
from fastapi import FastAPI
from app.routes.gateway import router as gateway_router
from app.routes.metrics import router as metrics_router
from app.routes.health import router as health_router

app = FastAPI(title="Nasiko Agent Request Layer")

app.include_router(gateway_router)
app.include_router(metrics_router)
app.include_router(health_router)

@app.get("/")
async def root():
    return {"message": "Nasiko Agent Request Layer Running"}
