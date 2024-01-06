from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.routers.auth.models import Order, Product, User


async def add_product_transaction(product_name: str, user_id: int, session: AsyncSession):
    product = Product(name=product_name, user_id=user_id, price=0)
    session.add(product)
    await session.commit()


async def add_user_transaction(user_name: str, user_email: str, session: AsyncSession):
    user = User(name=user_name, email=user_email)
    session.add(user)
    await session.commit()


async def add_order_transaction(
    product_id: int, user_id: int, quantity: int, session: AsyncSession
):
    order = Order(product_id=product_id, quantity=quantity, user_id=user_id)
    session.add(order)
    await session.commit()


async def get_user_products_transaction(user_id: int, session: AsyncSession):
    stmt = select(User).options(selectinload(User.products)).filter(User.id == user_id)
    user_object = await session.scalars(stmt)
    return user_object.first()
