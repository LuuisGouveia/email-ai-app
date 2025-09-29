from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import nltk
from ai_service import classify_and_reply
from nlp_utils import preprocess_text

nltk.download("punkt")
nltk.download("stopwords")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process-email")
async def process_email(
    file: UploadFile = None,
    text: str = Form(None)
):
    content = ""
    if file:
        if file.filename.endswith(".txt"):
            content = (await file.read()).decode("utf-8")
        elif file.filename.endswith(".pdf"):
            with pdfplumber.open(file.file) as pdf:
                content = "\n".join([page.extract_text() for page in pdf.page.extract_text()])
        elif text:
            content = text
        if not content:
                return {"error": "Nenhum conteudo enviado."}
        
        processed = preprocess_text(contet)
        categoria, resposta = classify_and_reply(processed)
        
        return {
            "categoria": categoria,
            "resposta" : resposta
        }
        