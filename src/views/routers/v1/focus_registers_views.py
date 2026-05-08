from fastapi import APIRouter, Request

from src.controllers.focus_registers_controller import FocusRegistersController
from src.controllers.services.focus_registers_service import (
    FocusRegisterService,
)
from src.models.config.database_session import get_session
from src.models.repositories.focus_repository import FocusRepository
from src.views.schemas.v1.focus_registers_schema import (
    FocusDataRequest,
    FocusDataResponse,
)

focus_registers_routers = APIRouter(prefix="/registro-foco")


@focus_registers_routers.post("", response_model=FocusDataResponse)
async def create_focus_register(request: Request, data: FocusDataRequest):
    async with get_session(request.app.state.engine) as session:
        repository = FocusRepository(session)
        service = FocusRegisterService(repository)
        controller = FocusRegistersController(service=service)
        return await controller.handle(data=data)
