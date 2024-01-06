import datetime

from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

from app.settings import settings


class DbHelper:
    @staticmethod
    async def create_session_object():
        engine = create_async_engine(settings.DATABASE.POSTGRES_DSN.unicode_string(), echo=True)
        async_session = async_sessionmaker(
            engine,
            expire_on_commit=False,
            autoflush=False,
        )
        return async_session

    @staticmethod
    async def get_session() -> AsyncSession:
        async_session = await DbHelper.create_session_object()
        async with async_session() as session:
            yield session


class BaseModel(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False, server_default=func.now(), onupdate=func.now()
    )

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"
