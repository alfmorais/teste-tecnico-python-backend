import pytest

from src.views.schemas.v1.diagnosis_productivity_schema import (
    DiagnosisProductivityResponse,
)


class TestDiagnosisProductivityResponse:
    @pytest.mark.asyncio
    async def test_should_create_response_successfully(self):
        response = DiagnosisProductivityResponse(
            average_focus_level=4.5,
            total_focus_time=120,
            feedback_message="Excelente nível de foco.",
        )

        assert response.average_focus_level == 4.5
        assert response.total_focus_time == 120
        assert response.feedback_message == ("Excelente nível de foco.")

    @pytest.mark.asyncio
    async def test_should_serialize_response_with_alias(self):
        response = DiagnosisProductivityResponse(
            average_focus_level=3.2,
            total_focus_time=90,
            feedback_message="Foco moderado.",
        )

        serialized_response = response.model_dump(
            by_alias=True,
        )

        assert serialized_response == {
            "media_nivel_foco": 3.2,
            "tempo_total_focado": 90,
            "mensagem_feedback": "Foco moderado.",
        }

    @pytest.mark.asyncio
    async def test_should_populate_using_alias_names(self):
        response = DiagnosisProductivityResponse(
            media_nivel_foco=5.0,
            tempo_total_focado=240,
            mensagem_feedback="Modo produtividade extrema.",
        )

        assert response.average_focus_level == 5.0
        assert response.total_focus_time == 240
        assert response.feedback_message == ("Modo produtividade extrema.")
