from db import settings
from typing import Any, AsyncContextManager, AsyncGenerator, Callable
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_async_engine(
    settings.DATABASE_URI,
    pool_pre_ping=True,
    future=True,
)
factory = async_sessionmaker(
    engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:  # noqa: WPS430, WPS442
    async with factory() as session:
        yield session