
from fastapi import APIRouter

router = APIRouter(prefix="/metrics", tags=["Metrics"])

cache_stats = {
    "hits": 0,
    "misses": 0
}

@router.get("/cache")
async def cache_metrics():
    return cache_stats

@router.get("/rate-limit")
async def rate_limit_metrics():
    return {
        "translator-agent": {
            "rpm": 100
        }
    }
