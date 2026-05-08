from unittest.mock import AsyncMock, MagicMock

import pytest

from src.controllers.diagnosis_productivity_controller import (
    DiagnosisProductivityController,
)
from src.models.entities.focus_entity import FocusTable
from src.views.schemas.v1.diagnosis_productivity_schema import (
    DiagnosisProductivityResponse,
)


class TestDiagnosisProductivityController:
    @pytest.fixture
    def service_mock(self):
        service = MagicMock()

        service.get_all_focus_registries = AsyncMock()
        service.get_average_focus_level = AsyncMock()
        service.get_total_focus_time = AsyncMock()
        service.get_comment_about_focus = AsyncMock()

        return service

    @pytest.fixture
    def controller(self, service_mock):
        return DiagnosisProductivityController(service=service_mock)

    @pytest.mark.asyncio
    async def test_should_return_default_response_when_no_registries(
        self, controller, service_mock
    ):
        service_mock.get_all_focus_registries.return_value = []

        result = await controller.handle()

        assert isinstance(result, DiagnosisProductivityResponse)
        assert result.average_focus_level == 0
        assert result.total_focus_time == 0
        assert result.feedback_message == "Nenhum registro encontrado."

    @pytest.mark.asyncio
    async def test_should_calculate_diagnosis_successfully(
        self, controller, service_mock
    ):
        fake_data = [
            FocusTable(id=1, focus_level=4, duration_minutes=30, comment="a"),
            FocusTable(id=2, focus_level=2, duration_minutes=60, comment="b"),
        ]

        service_mock.get_all_focus_registries.return_value = fake_data
        service_mock.get_average_focus_level.return_value = 3.0
        service_mock.get_total_focus_time.return_value = 90
        service_mock.get_comment_about_focus.return_value = "ok"

        result = await controller.handle()

        service_mock.get_all_focus_registries.assert_awaited_once()
        service_mock.get_average_focus_level.assert_awaited_once_with(
            focus_registries=fake_data
        )
        service_mock.get_total_focus_time.assert_awaited_once_with(
            focus_registries=fake_data
        )
        service_mock.get_comment_about_focus.assert_awaited_once_with(
            average_focus_level=3.0
        )

        assert result.average_focus_level == 3.0
        assert result.total_focus_time == 90
        assert result.feedback_message == "ok"
