from src.controllers.interfaces.focus_registers_interface import (
    FocusRegistersInterface,
)
from src.models.entities.focus_entity import FocusTable
from src.models.repositories.focus_repository import FocusRepository
from src.views.schemas.v1.focus_registers_schema import (
    FocusDataRequest,
    FocusDataResponse,
)


class FocusRegisterService(FocusRegistersInterface):
    def __init__(self, repository: FocusRepository) -> None:
        self.repository = repository

    async def create_focus_registry(
        self,
        data: FocusDataRequest,
    ) -> FocusDataResponse:
        focus_instance: FocusTable = await self.repository.create_focus(data)
        return FocusDataResponse.model_validate(focus_instance.model_dump())
