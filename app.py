import streamlit as st
from agents.doc_agent import DocumentAgent
from agents.chat_agent import ChatAgent
from agents.web_agent import WebAgent
from core.message_memory import ChatMemory

st.set_page_config(layout="wide", page_title="RAG Chatbot")

if 'memory' not in st.session_state:
    st.session_state.memory = ChatMemory()
    st.session_state.doc_agent = DocumentAgent()
    st.session_state.chat_agent = ChatAgent()
    st.session_state.web_agent = WebAgent()

st.title("📚 Agent-based Retrieval-Augmented Generation (RAG) Chatbot")

col1, col2 = st.columns([1, 1])

with col2:
    st.subheader("📄 Upload a File")
    uploaded_file = st.file_uploader("PDF / DOCX / TXT", type=["pdf", "docx", "txt"])
    if uploaded_file:
        text = st.session_state.doc_agent.load_and_index(uploaded_file)
        st.success("Document loaded and indexed ✅")
        st.text_area("Preview", text[:3000], height=300)

with col1:
    st.subheader("💬 Chat History")
    for msg in st.session_state.memory.history:
        with st.chat_message(msg['role']):
            st.markdown(msg['content'])

user_input = st.chat_input("Ask your question about the doc (or web)...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.memory.add("user", user_input)

    try:
        context = st.session_state.doc_agent.query(user_input)
        if context:
            answer = st.session_state.chat_agent.answer(user_input, context)
        else:
            raise ValueError("No context found.")
    except Exception as e:
        answer = st.session_state.web_agent.search(user_input)

    st.chat_message("assistant").markdown(answer)
    st.session_state.memory.add("assistant", answer)