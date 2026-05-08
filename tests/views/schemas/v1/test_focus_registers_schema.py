from datetime import datetime

import pytest
from pydantic import ValidationError

from src.views.schemas.v1.focus_registers_schema import (
    FocusDataRequest,
    FocusDataResponse,
)


class TestFocusDataRequest:
    @pytest.mark.asyncio
    async def test_should_create_focus_request_successfully(self):
        request = FocusDataRequest(
            nivel_foco=5,
            tempo_minutos=90,
            comentario="Estudando FastAPI",
        )

        assert request.focus_level == 5
        assert request.duration_minutes == 90
        assert request.comment == "Estudando FastAPI"

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        (
            "focus_level",
            "duration_minutes",
            "comment",
        ),
        [
            (0, 0, "Teste"),
            (6, 0, "Teste"),
            (-1, 0, "Teste"),
        ],
    )
    async def test_should_raise_error_when_focus_level_is_invalid(
        self,
        focus_level: int,
        duration_minutes: int,
        comment: str,
    ):
        with pytest.raises(ValidationError) as error:
            FocusDataRequest(
                nivel_foco=focus_level,
                tempo_minutos=duration_minutes,
                comentario=comment,
            )

        assert error.typename == "ValidationError"

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        (
            "focus_level",
            "duration_minutes",
            "comment",
        ),
        [
            (3, 0, "Teste"),
            (3, -10, "Teste"),
        ],
    )
    async def test_should_raise_error_when_duration_minutes_is_invalid(
        self,
        focus_level: int,
        duration_minutes: int,
        comment: str,
    ):
        with pytest.raises(ValidationError):
            FocusDataRequest(
                nivel_foco=focus_level,
                tempo_minutos=duration_minutes,
                comentario=comment,
            )

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        (
            "focus_level",
            "duration_minutes",
            "comment",
        ),
        [
            (3, 30, ""),
            (3, 30, None),
        ],
    )
    async def test_should_raise_error_when_comment_is_invalid(
        self,
        focus_level: int,
        duration_minutes: int,
        comment: str,
    ):
        with pytest.raises(ValidationError):
            FocusDataRequest(
                nivel_foco=focus_level,
                tempo_minutos=duration_minutes,
                comentario=comment,
            )


class TestFocusDataResponse:
    @pytest.mark.asyncio
    async def test_should_create_focus_response_successfully(
        self,
    ):
        created_at = datetime.now()

        response = FocusDataResponse(
            id=1,
            focus_level=5,
            duration_minutes=120,
            comment="Deep work",
            created_at=created_at,
        )

        assert response.id == 1
        assert response.focus_level == 5
        assert response.duration_minutes == 120
        assert response.comment == "Deep work"
        assert response.created_at == created_at

    @pytest.mark.asyncio
    async def test_should_serialize_response_using_alias(
        self,
    ):
        created_at = datetime.now()

        response = FocusDataResponse(
            id=1,
            focus_level=4,
            duration_minutes=60,
            comment="API Development",
            created_at=created_at,
        )

        serialized_response = response.model_dump(
            by_alias=True,
        )

        assert serialized_response == {
            "id": 1,
            "nivel_foco": 4,
            "tempo_minutos": 60,
            "comentario": "API Development",
            "data_criacao": created_at,
        }

    @pytest.mark.asyncio
    async def test_should_create_response_using_alias_fields(
        self,
    ):
        created_at = datetime.now()

        response = FocusDataResponse(
            id=1,
            nivel_foco=5,
            tempo_minutos=180,
            comentario="Sessão de foco",
            data_criacao=created_at,
        )

        assert response.focus_level == 5
        assert response.duration_minutes == 180
        assert response.comment == "Sessão de foco"
        assert response.created_at == created_at

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        ("response_data",),
        [
            (
                {
                    "id": 1,
                    "focus_level": 6,
                    "duration_minutes": 60,
                    "comment": "Teste",
                    "created_at": datetime.now(),
                },
            ),
            (
                {
                    "id": 1,
                    "focus_level": 0,
                    "duration_minutes": 60,
                    "comment": "Teste",
                    "created_at": datetime.now(),
                },
            ),
            (
                {
                    "id": 1,
                    "focus_level": 3,
                    "duration_minutes": 0,
                    "comment": "Teste",
                    "created_at": datetime.now(),
                },
            ),
            (
                {
                    "id": 1,
                    "focus_level": 3,
                    "duration_minutes": 60,
                    "comment": None,
                    "created_at": datetime.now(),
                },
            ),
        ],
    )
    async def test_should_raise_error_when_response_data_is_invalid(
        self,
        response_data: dict,
    ):
        with pytest.raises(ValidationError):
            FocusDataResponse(**response_data)
