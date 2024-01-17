from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.helpers.jwt import hash_password
from app.routers.auth.models import User
from app.routers.auth.schemas import UserCreateSchema


async def get_user_by_email(session: AsyncSession, email: str):
    user = await session.scalars(select(User).where(User.email == email))
    return user.first()


async def create_user(session: AsyncSession, user_schema: UserCreateSchema):
    user_schema.password = hash_password(user_schema.password).decode()
    user = User(**user_schema.model_dump())
    session.add(user)
    await session.commit()
