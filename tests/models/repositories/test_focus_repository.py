from unittest.mock import AsyncMock, MagicMock

import pytest

from src.models.entities.focus_entity import FocusTable
from src.models.repositories.focus_repository import FocusRepository
from src.views.schemas.v1.focus_registers_schema import FocusDataRequest


class TestFocusRepository:
    @pytest.fixture
    def db_mock(self):
        db = MagicMock()
        db.add = MagicMock()
        db.commit = AsyncMock()
        db.refresh = AsyncMock()
        db.execute = AsyncMock()
        return db

    @pytest.fixture
    def repository(self, db_mock):
        return FocusRepository(db=db_mock)

    @pytest.mark.asyncio
    async def test_should_create_focus_successfully(self, repository, db_mock):
        request = FocusDataRequest(
            nivel_foco=5,
            tempo_minutos=60,
            comentario="study",
        )

        result = await repository.create_focus(request)

        db_mock.add.assert_called_once()
        db_mock.commit.assert_awaited_once()
        db_mock.refresh.assert_awaited_once()

        assert isinstance(result, FocusTable)
        assert result.focus_level == 5
        assert result.duration_minutes == 60
        assert result.comment == "study"

    @pytest.mark.asyncio
    async def test_should_retrieve_focus_successfully(
        self, repository, db_mock
    ):
        focus_list = [
            FocusTable(
                id=1,
                focus_level=4,
                duration_minutes=30,
                comment="a",
            )
        ]

        scalars_mock = MagicMock()
        scalars_mock.all.return_value = focus_list

        result_mock = MagicMock()
        result_mock.scalars.return_value = scalars_mock

        db_mock.exec = AsyncMock(return_value=result_mock)

        result = await repository.retrieve_focus()

        db_mock.exec.assert_awaited_once()

        assert result == focus_list
