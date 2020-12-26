from fastapi import APIRouter

from api.endpoints import detections

api_router = APIRouter()
api_router.include_router(detections.router, tags=["detections"])