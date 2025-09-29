import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import pytest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    
def test_process_email_with_text(monkeypatch):
    def fake_classify_and_replay(text):
        return "Produtivo", "Resposta teste"
    
    monkeypatch.setattr("backend.app.classify_and_reply", fake_classify_and_reply)

    response = client.post("/process-email", data={"text": "Email de teste"})
    assert response.status_code == 200
    data = response.json()
    assert data["categoria"] == "Produtivo"
    assert data["resposta"] == "Resposta teste"
    
def test_process_email_without_content():
    response = client.post("/process-email", data={})
    assert response.status_code == 200
    data = response.json()
    assert "error" in data