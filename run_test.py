import nltk

for pkg in ["punkt", "stopwords", "punkt_tab"]:
    nltk.download(pkg, quiet=True)

from backend.ai_service import classify_and_reply
from backend.nlp_utils import preprocess_text

text = "Precisamos de uma cotação para um serviço de consultoria de marketing."
processed = preprocess_text(text)
categoria, resposta = classify_and_reply(processed)
print("Categoria:", categoria)
print("Resposta:", resposta)