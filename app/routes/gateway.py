
from fastapi import APIRouter
from app.middleware.cache import get_cache, set_cache
from app.middleware.rate_limiter import allow_request
from app.services.agent_router import process_agent_request

router = APIRouter(prefix="/gateway", tags=["Gateway"])

@router.post("/request")
async def handle_request(payload: dict):
    agent = payload.get("agent")
    query = payload.get("query")

    cache_key = f"{agent}:{query}"

    cached = get_cache(cache_key)
    if cached:
        return {
            "source": "cache",
            "response": cached
        }

    allowed = allow_request(agent)

    if not allowed:
        return {
            "status": "queued",
            "message": "Rate limit exceeded"
        }

    response = process_agent_request(agent, query)

    set_cache(cache_key, response)

    return {
        "source": "agent",
        "response": response
    }
