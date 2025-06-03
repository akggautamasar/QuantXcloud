import os
import subprocess

port = os.getenv("PORT", "8000")
subprocess.run(["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", port])
