from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.controllers.services.diagnosis_productivity_service import (
    DiagnosisProductivityService,
)
from src.models.entities.focus_entity import FocusTable


class TestDiagnosisProductivityService:
    @pytest.fixture
    def repository_mock(self):
        repo = MagicMock()
        repo.retrieve_focus = AsyncMock()
        return repo

    @pytest.fixture
    def service(self, repository_mock):
        return DiagnosisProductivityService(repository=repository_mock)

    @pytest.mark.asyncio
    async def test_should_get_all_focus_registries(
        self, service, repository_mock
    ):
        fake_data = [
            FocusTable(
                id=1,
                focus_level=4,
                duration_minutes=30,
                comment="study",
            )
        ]

        repository_mock.retrieve_focus.return_value = fake_data

        result = await service.get_all_focus_registries()

        assert result == fake_data
        repository_mock.retrieve_focus.assert_called_once()

    @pytest.mark.asyncio
    async def test_should_calculate_average_focus_level(self, service):
        data = [
            FocusTable(id=1, focus_level=4, duration_minutes=10, comment="a"),
            FocusTable(id=2, focus_level=2, duration_minutes=20, comment="b"),
        ]

        result = await service.get_average_focus_level(data)

        assert result == 3.0

    @pytest.mark.asyncio
    async def test_should_calculate_total_focus_time(self, service):
        data = [
            FocusTable(id=1, focus_level=4, duration_minutes=10, comment="a"),
            FocusTable(id=2, focus_level=2, duration_minutes=20, comment="b"),
        ]

        result = await service.get_total_focus_time(data)

        assert result == 30

    @pytest.mark.asyncio
    async def test_should_return_high_focus_message(self, service):
        with patch("random.choice", return_value="HIGH_MESSAGE"):
            result = await service.get_comment_about_focus(4.5)
            assert result == "HIGH_MESSAGE"

    @pytest.mark.asyncio
    async def test_should_return_low_focus_message(self, service):
        with patch("random.choice", return_value="LOW_MESSAGE"):
            result = await service.get_comment_about_focus(2.0)
            assert result == "LOW_MESSAGE"

    @pytest.mark.asyncio
    async def test_should_raise_error_when_empty_list(self, service):
        with pytest.raises(ZeroDivisionError):
            await service.get_average_focus_level([])
