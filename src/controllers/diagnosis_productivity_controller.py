from src.controllers.base_controller import BaseController
from src.controllers.interfaces.diagnosis_productivity_interface import (
    DiagnosisProductivityInterface,
)
from src.views.schemas.v1.diagnosis_productivity_schema import (
    DiagnosisProductivityResponse,
)


class DiagnosisProductivityController(BaseController):
    def __init__(self, service: DiagnosisProductivityInterface) -> None:
        self.service = service

    async def handle(self, data: None = None) -> DiagnosisProductivityResponse:
        focus_registries = await self.service.get_all_focus_registries()

        if not focus_registries:
            response_data = {
                "average_focus_level": 0,
                "total_focus_time": 0,
                "feedback_message": "Nenhum registro encontrado.",
            }
            return DiagnosisProductivityResponse(**response_data)

        average_focus_level = await self.service.get_average_focus_level(
            focus_registries=focus_registries
        )
        total_focus_time = await self.service.get_total_focus_time(
            focus_registries=focus_registries
        )
        feedback_message = await self.service.get_comment_about_focus(
            average_focus_level=average_focus_level,
        )

        response_data = {
            "average_focus_level": average_focus_level,
            "total_focus_time": total_focus_time,
            "feedback_message": feedback_message,
        }
        return DiagnosisProductivityResponse(**response_data)
