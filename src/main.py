from fastapi import FastAPI

from src.lifespan import lifespan
from src.views.routers.v1.diagnosis_productivity_view import (
    diagnosis_productivity_router,
)
from src.views.routers.v1.focus_registers_views import focus_registers_routers

app = FastAPI(lifespan=lifespan)
app.include_router(diagnosis_productivity_router)
app.include_router(focus_registers_routers)
