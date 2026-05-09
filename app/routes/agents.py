from fastapi import APIRouter

router = APIRouter(prefix="/agents", tags=["Agents"])


@router.get("/translator/health")
async def translator_health():
    return {
        "agent": "translator",
        "status": "healthy",
        "deployment": "local",
    }
