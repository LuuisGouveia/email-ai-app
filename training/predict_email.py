from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


model_path = "./saved_models/email_classifier"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)


id2label = {0: "Produtivo", 1: "Improdutivo"}

def predict_email(text):
    
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

   
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_id = torch.argmax(logits, dim=1).item()
    
    return id2label[predicted_class_id]


if __name__ == "__main__":
    emails = [
        "Preciso terminar o relatório de vendas até amanhã.",
        "Assista ao vídeo engraçado no YouTube e relaxe.",
        "Reunião importante com o cliente às 14h.",
        "Jogando videogame durante o horário de trabalho."
    ]

    for email in emails:
        categoria = predict_email(email)
        print(f"Email: {email}\nCategoria prevista: {categoria}\n")
