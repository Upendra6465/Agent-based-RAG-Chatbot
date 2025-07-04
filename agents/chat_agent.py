from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class ChatAgent:
    def __init__(self):
        self.model_name = "google/flan-t5-base"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

    def answer(self, query, chunks):
        context = "\n".join(chunks)
        prompt = f"Answer the question using the context.\n\nContext: {context}\n\nQuestion: {query}"
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        outputs = self.model.generate(**inputs, max_new_tokens=250)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)