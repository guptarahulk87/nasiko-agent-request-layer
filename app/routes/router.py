from fastapi import APIRouter

router = APIRouter(prefix="/router", tags=["Router"])


@router.get("/route")
async def route_query(query: str):
    selected_agent = "translator" if "translate" in query.lower() else "default"

    return {
        "query": query,
        "agent": selected_agent,
        "route": f"/agents/{selected_agent}",
    }
