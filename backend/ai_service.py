import random
from transformers import pipeline


classifier = pipeline(
    "text-classification",
    model="luuisgouveia/email-classifier",
    tokenizer="luuisgouveia/email-classifier"
)


produtivo_templates = [
    "Olá! Obrigado pela mensagem. Vamos dar andamento ao assunto: '{}...'",
    "Recebido! Vamos prosseguir com: '{}...'",
    "Agradecemos o envio. Iremos trabalhar no seguinte ponto: '{}...'"
]

improdutivo_templates = [
    "Olá! Recebemos sua mensagem. Caso queira adicionar mais detalhes, fique à vontade.",
    "Mensagem registrada. Se houver algo importante, por favor nos envie.",
    "Obrigado pelo envio! Para dar andamento, por favor envie mais informações se necessário."
]

def classify_and_reply(text: str):

    result = classifier(text)[0]
    label = result['label']


    categoria = label

    if categoria == "Produtivo":
        resposta = random.choice(produtivo_templates).format(text[:50])
    else:
        resposta = random.choice(improdutivo_templates)

    return categoria, resposta
