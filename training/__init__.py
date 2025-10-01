from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer


dataset = load_dataset("csv", data_files={
    "train": "training/emails.csv",
    "test": "training/emails_test.csv"
})


tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)

dataset = dataset.map(tokenize, batched=True)


model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)


training_args = TrainingArguments(
    output_dir="./saved_models/email_classifier",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    learning_rate=2e-5,
    weight_decay=0.01,
)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
)


trainer.train()


trainer.save_model("./saved_models/email_classifier")
tokenizer.save_pretrained("./saved_models/email_classifier")
