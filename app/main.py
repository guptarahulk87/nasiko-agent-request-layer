
from fastapi import FastAPI
from app.routes.app_ui import router as app_ui_router
from app.routes.agents import router as agents_router
from app.routes.gateway import router as gateway_router
from app.routes.metrics import router as metrics_router
from app.routes.health import router as health_router
from app.routes.router import router as router_router

app = FastAPI(title="Nasiko Agent Request Layer")

app.include_router(app_ui_router)
app.include_router(agents_router)
app.include_router(gateway_router)
app.include_router(metrics_router)
app.include_router(health_router)
app.include_router(router_router)

@app.get("/")
async def root():
    return {"message": "Nasiko Agent Request Layer Running"}
