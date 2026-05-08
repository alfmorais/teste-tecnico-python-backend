from abc import ABC, abstractmethod

from src.views.schemas.v1.focus_registers_schema import (
    FocusDataRequest,
    FocusDataResponse,
)


class FocusRegistersInterface(ABC):
    @abstractmethod
    async def create_focus_registry(
        self, data: FocusDataRequest
    ) -> FocusDataResponse:
        pass
