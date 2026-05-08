from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.models.config.database_engine import (
    create_db_and_tables,
    create_engine,
)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    app.state.engine = await create_engine()

    await create_db_and_tables(app.state.engine)

    yield

    await app.state.engine.dispose()
