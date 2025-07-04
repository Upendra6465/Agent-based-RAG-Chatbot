import fitz  # PyMuPDF
import docx

def parse_file(file):
    ext = file.name.split(".")[-1]
    if ext == "pdf":
        return extract_pdf(file)
    elif ext == "docx":
        return extract_docx(file)
    elif ext == "txt":
        return file.read().decode("utf-8")
    else:
        return "Unsupported file type"

def extract_pdf(file):
    text = ""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

def extract_docx(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs])