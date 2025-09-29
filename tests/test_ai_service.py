import pytest
from backend import ai_service

def test_classifyand_reply(monkeypatch):
    def fake_chatcompletion_create(*args, **kwargs):
        class FakeChoice:
            message = type("msg", (), {"content": "Produtivo"})
        return type("resp", (), {"choices": [FakeChoice()]})
    
    monkeypatch.setattr("openai.ChatCompletion.create", fake_chatcompletion_create)
    
    
    categoria, resposta = ai_service.classify_and_reply("teste")
    assert categoria in ["Produtivo", "Improdutivo"]
    assert isinstance(resposta, str)
    