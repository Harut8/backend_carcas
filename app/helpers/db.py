from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from app.settings import settings


class DbHelper:
    @staticmethod
    async def create_session():
        engine = create_async_engine(settings.POSTGRES_DSN.unicode_string())
        async_session = async_sessionmaker(
            engine,
            expire_on_commit=False,
            autoflush=False,
        )
        return async_session

    @staticmethod
    async def get_session() -> AsyncSession:
        async_session = await DbHelper.create_session()
        async with async_session() as session:
            yield session


