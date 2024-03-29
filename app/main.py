from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from app.helpers.db import DbHelper
from app.routers.auth.auth import auth_router
from app.settings import settings

app = FastAPI()

app.include_router(auth_router, prefix=settings.API_V1_PREFIX)


@app.get("/health-check")
async def health_check(session: AsyncSession = Depends(DbHelper.get_session)):
    return {"message": "App is up and running!"}
