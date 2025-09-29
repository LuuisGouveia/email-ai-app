import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_and_reply(text: str):
    
    classification_prompt = f"""
    Classifique o seguinte email como "Produtivo" ou "Improdutivo".
    Texto: {text}
    Responda somente com uma palavra: Produtivo ou Improdutivo;
    """
    cls = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": classification_prompt}],
        temperature=0
    )
    categoria = cls.choices[0].message.content.strip()
    
    reply_prompt = f"""
    Gere uma resposta automática curta e educada para um email classificado como {categoria}.
    Texto: {text}
    """
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": reply_prompt}],
        temperature=0.7
    )
    resposta = resp.choices[0].message.content.strip()
    return categoria, resposta