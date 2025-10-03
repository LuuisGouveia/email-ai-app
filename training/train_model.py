import os
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer


os.makedirs("./saved_models/email_classifier", exist_ok=True)


dataset = load_dataset("csv", data_files={
    "train": "training/emails.csv",
    "test": "training/emails_test.csv"
})


label_map = {"Produtivo": 0, "Improdutivo": 1}
id2label = {0: "Produtivo", 1: "Improdutivo"}

def encode_labels(batch):
    batch["label"] = label_map[batch["label"]]
    return batch

dataset = dataset.map(encode_labels)


tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)

dataset = dataset.map(tokenize, batched=True)


model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=2,
    id2label=id2label,
    label2id=label_map
)


training_args = TrainingArguments(
    output_dir="./saved_models/email_classifier",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=10,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    save_total_limit=1,
    load_best_model_at_end=True,
    eval_strategy="epoch",
    save_strategy="epoch"
)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
)

trainer.train()


model.save_pretrained("./saved_models/email_classifier") 
tokenizer.save_pretrained("./saved_models/email_classifier")


print("Treinamento finalizado e modelo salvo em ./saved_models/email_classifier")
