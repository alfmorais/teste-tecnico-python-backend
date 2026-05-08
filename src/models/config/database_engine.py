from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
)
from sqlmodel import SQLModel

from src.models.entities.focus_entity import FocusTable  # noqa: F401

DATABASE_URL = "sqlite+aiosqlite:///database.db"


async def create_engine() -> AsyncEngine:
    engine: AsyncEngine = create_async_engine(
        DATABASE_URL,
        echo=False,
    )
    return engine


async def create_db_and_tables(engine: AsyncEngine) -> None:
    async with engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.create_all)
