# Exemplo de como você pode reestruturar o carregamento do modelo:

import random
import os
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

model_name = "luuisgouveia/email-classifier"
CLASSIFIER = None

def get_classifier():
    
    global CLASSIFIER

    if CLASSIFIER is None:
        print("--- Carregando modelo na memória pela primeira vez... ---")
        
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=os.getenv("HF_TOKEN"))
        model = AutoModelForSequenceClassification.from_pretrained(model_name, use_auth_token=os.getenv("HF_TOKEN"))
        
       
        CLASSIFIER = pipeline(
            "text-classification",
            model=model,
            tokenizer=tokenizer
        )
        print("--- Modelo carregado com sucesso. ---")
    
    return CLASSIFIER



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
    
    classifier = get_classifier() 
    
    result = classifier(text)[0]
    label = result['label']
    
    
    categoria = label

    if categoria == "Produtivo":
        resposta = random.choice(produtivo_templates).format(text[:50])
    else:
        resposta = random.choice(improdutivo_templates)

    return categoria, resposta

