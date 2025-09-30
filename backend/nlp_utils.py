import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

for resource in ["punkt", "stopwords"]:
    try:
        nltk.data.find(f"tokenizers/{resource}" if resource == "punkt" else f"corpora/{resource}")
    except LookupError:
        nltk.download(resource)

def preprocess_text(text: str) -> str:
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words("portuguese"))
    tokens = [t for t in tokens if t not in stop_words and t not in string.punctuation]
    return " ".join(tokens)
