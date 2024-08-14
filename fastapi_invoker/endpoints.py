from fastapi import APIRouter
from pydantic import BaseModel
from services import runcascade
from cache import Cache

router = APIRouter()
cache = Cache()


class RecommendationRequest(BaseModel):
    viewer_id: int


@router.post("/recommend")
async def recommend(request: RecommendationRequest):
    viewer_id = request.viewer_id

    cached_result = cache.get(viewer_id)
    if cached_result:
        return cached_result

    result = await runcascade()
    cache.set(viewer_id, result)
    return result
