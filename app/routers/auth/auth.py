from fastapi import APIRouter
from app.settings import settings

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.get("/health-check")
async def health_check():
    return {"message": "App is up and running!"}
