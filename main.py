cat << 'EOF' > main.py
from fastapi import FastAPI
import platform
import psutil
import datetime

app = FastAPI(
    title="DevOps Health Monitor",
    description="Lightweight API showing server health and version info.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "DevOps Health API is running successfully."}

@app.get("/health")
def health_check():
    return {"status": "OK", "timestamp": datetime.datetime.utcnow()}

@app.get("/version")
def version():
    return {
        "app_version": "1.0.0",
        "python_version": platform.python_version(),
        "platform": platform.system()
    }

@app.get("/metrics")
def metrics():
    return {
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent
    }
EOF

