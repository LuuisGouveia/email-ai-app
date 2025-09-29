from backend.nlp_utils import preprocess_text

def test_preprocess_removes_stopwords():
    text = "Eu estou escrevendo um email importante"
    processed = preprocess_text(text)
    assert "email" in processed
    assert "importante" in processed
    assert "eu" not in processed
    