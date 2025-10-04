from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import nltk
from .ai_service import classify_and_reply
from .nlp_utils import preprocess_text
from fastapi.staticfiles import StaticFiles
from fastapi.routing import APIRoute

nltk.download("punkt")
nltk.download("stopwords")

app = FastAPI()




origins = [
    "https://luuisgouveia.github.io",
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get("/health")
def healthcheck():
    return {"status": "ok"}

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
                content = "\n".join([page.extract_text() or "" for page in pdf.pages])

    
    if not content and text:
        content = text

    if not content:
        return {"error": "Nenhum conteúdo enviado."}
        
    processed = preprocess_text(content)
    categoria, resposta = classify_and_reply(processed)
        
    return {
            "categoria": categoria,
            "resposta" : resposta
        }



@app.on_event("startup")
def show_routes():
    print("\n=== ROTAS REGISTRADAS ===")
    for route in app.routes:
        if hasattr(route, "methods"):
            methods = ",".join(route.methods)
            print(f"{route.path} -> {methods}")
    print("=========================\n")
