import os

port = os.getenv("PORT", "8000")
os.system(f"python -m uvicorn main:app --host 0.0.0.0 --port {port}")
