from fastapi import FastAPI
from app.api.routes import router
from app.core.logger import setup_logging

setup_logging()

app = FastAPI(
    title="CI-CD Ready Python App",
    description="FastAPI app for DevOps CI/CD & Kubernetes demos",
    version="1.0.0"
)

app.include_router(router)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "UP"}
