from transformers import AutoModelForSequenceClassification, AutoTokenizer

repo_id = "luuisgouveia/email-classifier"

model = AutoModelForSequenceClassification.from_pretrained("./saved_models/email_classifier")
tokenizer = AutoTokenizer.from_pretrained("./saved_models/email_classifier")

model.push_to_hub(repo_id)
tokenizer.push_to_hub(repo_id)

print(f"🚀 Modelo enviado para o Hub em https://huggingface.co/{repo_id}")