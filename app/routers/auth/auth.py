from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.helpers.db import DbHelper
from app.routers.auth.crud import (
    add_product_transaction,
    add_user_transaction,
    get_user_products_transaction,
)

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.get("/health-check")
async def health_check():
    return {"message": "App is up and running!"}


@auth_router.post("/add-product")
async def add_product(
    product_name: str, user_id: int, session: AsyncSession = Depends(DbHelper.get_session)
):
    await add_product_transaction(product_name=product_name, user_id=user_id, session=session)


@auth_router.post("/add-user")
async def add_user(
    user_name: str, user_email: str, session: AsyncSession = Depends(DbHelper.get_session)
):
    await add_user_transaction(user_name=user_name, user_email=user_email, session=session)


@auth_router.get("/user-products")
async def add_order(user_id: int, session: AsyncSession = Depends(DbHelper.get_session)):
    user = await get_user_products_transaction(user_id, session)
    return user
