from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI Healthcheck running successfully"}

@app.get("/health")
def health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    return {
        "status": "healthy",
        "cpu_usage": cpu,
        "memory_usage": memory,
        "disk_usage": disk
    }
