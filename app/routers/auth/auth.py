from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.get("/health-check")
async def health_check():
    return {"message": "App is up and running!"}
