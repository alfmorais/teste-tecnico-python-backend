from unittest.mock import AsyncMock, MagicMock

import pytest

from src.controllers.services.focus_registers_service import (
    FocusRegisterService,
)
from src.models.entities.focus_entity import FocusTable
from src.views.schemas.v1.focus_registers_schema import (
    FocusDataRequest,
    FocusDataResponse,
)


class TestFocusRegisterService:
    @pytest.fixture
    def repository_mock(self):
        repo = MagicMock()
        repo.create_focus = AsyncMock()
        return repo

    @pytest.fixture
    def service(self, repository_mock):
        return FocusRegisterService(repository=repository_mock)

    @pytest.mark.asyncio
    async def test_should_create_focus_registry_successfully(
        self, service, repository_mock
    ):
        request = FocusDataRequest(
            nivel_foco=5, tempo_minutos=60, comentario="study"
        )

        focus_entity = FocusTable(
            id=1, focus_level=5, duration_minutes=60, comment="study"
        )

        repository_mock.create_focus.return_value = focus_entity

        result = await service.create_focus_registry(request)

        assert isinstance(result, FocusDataResponse)
        assert result.id == 1
        assert result.focus_level == 5
        assert result.duration_minutes == 60
        assert result.comment == "study"

        repository_mock.create_focus.assert_called_once_with(request)
