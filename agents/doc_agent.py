import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from utils.file_parser import parse_file

class DocumentAgent:
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
        self.index = faiss.IndexFlatL2(384)
        self.chunks = []
        self.chunk_map = {}

    def split_text_sliding_window(self, text, chunk_size=1000, overlap=200):
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size - overlap)]

    def load_and_index(self, uploaded_file):
        raw_text = parse_file(uploaded_file)
        chunks = self.split_text_sliding_window(raw_text)
        self.chunks = chunks
        embeddings = self.embedder.encode(chunks, convert_to_numpy=True, show_progress_bar=False)
        self.index = faiss.IndexFlatL2(384)
        self.index.add(np.array(embeddings))
        self.chunk_map = {i: chunk for i, chunk in enumerate(chunks)}
        return raw_text

    def query(self, question, top_k=6):
        q_emb = self.embedder.encode([question], convert_to_numpy=True)
        D, I = self.index.search(np.array(q_emb), top_k)
        return [self.chunk_map[i] for i in I[0] if i in self.chunk_map]