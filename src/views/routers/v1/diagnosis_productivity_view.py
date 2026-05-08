from fastapi import APIRouter, Request

from src.controllers.diagnosis_productivity_controller import (
    DiagnosisProductivityController,
)
from src.controllers.services.diagnosis_productivity_service import (
    DiagnosisProductivityService,
)
from src.models.config.database_session import get_session
from src.models.repositories.focus_repository import FocusRepository

diagnosis_productivity_router = APIRouter(prefix="/diagnostico-produtividade")


@diagnosis_productivity_router.get("")
async def get_diagnosis_productivity_registry(request: Request):
    async with get_session(request.app.state.engine) as session:
        repository = FocusRepository(db=session)
        service = DiagnosisProductivityService(repository=repository)
        controller = DiagnosisProductivityController(service=service)
        return await controller.handle()
