from fastapi import APIRouter
from pydantic import BaseModel
import torch
from app.core.model_loader import model, tokenizer, device

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/predict")
def predict(data: TextRequest):
    inputs = tokenizer(
        data.text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        confidence, pred = torch.max(probs, dim=1)

    label = "Sarcastic" if pred.item() == 1 else "Not Sarcastic"

    return {
        "prediction": label,
        "confidence": round(confidence.item(), 4)
    }
