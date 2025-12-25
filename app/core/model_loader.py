import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_PATH = "model/sarcasm_model"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.to(device)
model.eval()
