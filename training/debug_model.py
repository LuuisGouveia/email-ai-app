from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model_path = "./saved_models/email_classifier"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

text = "Preciso terminar o relatório de vendas até amanhã."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

print("Logits:", outputs.logits)
print("Predição:", torch.argmax(outputs.logits, dim=1).item())
