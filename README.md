# Weathera AI Service

FastAPI service that asks an LLM what to wear for a given forecast.
The mobile app calls it; the LLM key never ships inside the app.

## Run locally

```bash
cd ai_service
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then fill in your keys
fastapi dev app/main.py     # http://127.0.0.1:8000/docs
```

## Test

```bash
pytest
```
