from fastapi import APIRouter

from app.api.routes import  audios

api_router = APIRouter()
api_router.include_router(audios.router, prefix="/audio", tags=["audio"])
