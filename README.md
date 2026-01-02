# Sarcasm Detection API (FastAPI)

This FastAPI app serves a local Transformers model for sarcasm detection.

## Deploy: Hugging Face Spaces (Docker)

1. Create a new Space: https://huggingface.co/spaces
   - Runtime: Docker
   - Space name: choose anything (e.g., `your-username/sarcasm-api`)
2. Upload/push these files to the Space repo:
   - `Dockerfile`
   - `requirements.txt`
   - `app/` (code)
   - `model/` (the `sarcasm_model` folder and its files)
3. The Space will build automatically. When it’s “Running”, your API is live.

Default port is managed by Spaces (`PORT`, usually 7860). The Dockerfile already binds to it.

## Local Run

```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000/docs to try endpoints.

## API Usage

- Base URL (Spaces): `https://huggingface.co/spaces/<username>/<space-name>`
- Predict endpoint: `POST /predict`

Example `curl`:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"text": "Yeah, sure, that was totally helpful."}' \
  https://huggingface.co/spaces/<username>/<space-name>/predict
```

Example Python client:

```python
import requests

url = "https://huggingface.co/spaces/<username>/<space-name>/predict"
payload = {"text": "What a brilliant idea..."}
r = requests.post(url, json=payload, timeout=30)
print(r.json())
```

Response format:

```json
{
  "prediction": "Sarcastic" | "Not Sarcastic",
  "confidence": 0.9876
}
```

## Notes

- Model files live under `model/sarcasm_model`. Ensure they’re present in the Space.
- Spaces hardware is CPU by default; performance depends on model size.
- For private usage or stronger SLAs, consider Hugging Face Inference Endpoints or a container host.
# sarcasm-detection-fast-api
# sarcasm-detection-fastapi-new
