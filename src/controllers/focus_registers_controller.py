from src.controllers.base_controller import BaseController
from src.controllers.interfaces.focus_registers_interface import (
    FocusRegistersInterface,
)
from src.views.schemas.v1.focus_registers_schema import (
    FocusDataRequest,
    FocusDataResponse,
)


class FocusRegistersController(BaseController):
    def __init__(self, service: FocusRegistersInterface) -> None:
        self.service = service

    async def handle(self, data: FocusDataRequest) -> FocusDataResponse:
        return await self.service.create_focus_registry(data=data)
