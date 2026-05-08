from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

import pytest

from src.controllers.focus_registers_controller import FocusRegistersController
from src.views.schemas.v1.focus_registers_schema import (
    FocusDataRequest,
    FocusDataResponse,
)


class TestFocusRegistersController:
    @pytest.fixture
    def service_mock(self):
        service = MagicMock()
        service.create_focus_registry = AsyncMock()
        return service

    @pytest.fixture
    def controller(self, service_mock):
        return FocusRegistersController(service=service_mock)

    @pytest.mark.asyncio
    async def test_should_create_focus_registry(
        self, controller, service_mock
    ):
        request = FocusDataRequest(
            nivel_foco=4,
            tempo_minutos=30,
            comentario="study",
        )

        expected_response = FocusDataResponse(
            id=1,
            focus_level=4,
            duration_minutes=30,
            comment="study",
            created_at=datetime.now(),
        )

        service_mock.create_focus_registry.return_value = expected_response

        result = await controller.handle(request)

        service_mock.create_focus_registry.assert_awaited_once_with(
            data=request
        )
        assert result == expected_response
