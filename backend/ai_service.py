from transformers import pipeline

# Carrega o modelo de análise de sentimento do Hugging Face
classifier = pipeline("sentiment-analysis")

def classify_and_reply(text: str):
    """
    Classifica o email como 'Produtivo' ou 'Improdutivo'
    e gera uma resposta automática.
    """

    # Classificação
    result = classifier(text)[0]
    label = result['label']

    # Ajusta para o teu domínio
    if label == "POSITIVE":
        categoria = "Produtivo"
    else:
        categoria = "Improdutivo"

    # Geração de resposta automática simples
    if categoria == "Produtivo":
        resposta = f"Olá! Obrigado pela sua mensagem. Vamos dar andamento ao conteúdo: '{text[:50]}...'"
    else:
        resposta = f"Olá! Recebemos sua mensagem. Caso tenha informações adicionais, por favor, nos envie."

    return categoria, resposta
