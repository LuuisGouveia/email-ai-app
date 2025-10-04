import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


required_resources = ["punkt", "stopwords", "punkt_tab"] 


for resource in required_resources:
    try:

        if resource == "punkt_tab":

             nltk.data.find(f"tokenizers/{resource}")
        elif resource == "punkt":

             nltk.data.find(f"tokenizers/{resource}")
        else:

             nltk.data.find(f"corpora/{resource}")
             
    except LookupError:
        print(f"Downloading missing NLTK resource: {resource}...")
        nltk.download(resource)


def preprocess_text(text: str) -> str:

    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words("portuguese"))
    tokens = [t for t in tokens if t not in stop_words and t not in string.punctuation]
    return " ".join(tokens)