from app.helpers.db import DbHelper
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()


@app.get("/health-check")
async def health_check(db_session: AsyncSession = Depends(DbHelper.create_session)):
    return {"message": "App is up and running!"}
