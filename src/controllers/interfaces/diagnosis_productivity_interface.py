from abc import ABC, abstractmethod

from src.models.entities.focus_entity import FocusTable


class DiagnosisProductivityInterface(ABC):
    @abstractmethod
    async def get_all_focus_registries(self) -> list[FocusTable]:
        pass

    @abstractmethod
    async def get_average_focus_level(
        self, focus_registries: list[FocusTable]
    ) -> float:
        pass

    @abstractmethod
    async def get_total_focus_time(
        self, focus_registries: list[FocusTable]
    ) -> int:
        pass

    @abstractmethod
    async def get_comment_about_focus(
        self,
        average_focus_level: float,
    ) -> str:
        pass
