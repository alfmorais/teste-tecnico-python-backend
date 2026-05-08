import pytest

from src.models.entities.focus_entity import FocusTable


class TestDiagnosisProductivityEndpoint:
    @pytest.mark.asyncio
    async def test_should_return_productivity_diagnosis_with_seeded_data(
        self, client, session, engine
    ):
        client.app.state.engine = engine

        session.add_all(
            [
                FocusTable(focus_level=5, duration_minutes=60, comment="a"),
                FocusTable(focus_level=4, duration_minutes=30, comment="b"),
                FocusTable(focus_level=3, duration_minutes=20, comment="c"),
                FocusTable(focus_level=2, duration_minutes=10, comment="d"),
                FocusTable(focus_level=5, duration_minutes=50, comment="e"),
                FocusTable(focus_level=4, duration_minutes=40, comment="f"),
            ]
        )
        await session.commit()

        response = client.get("/diagnostico-produtividade")

        assert response.status_code == 200

        data = response.json()

        assert "media_nivel_foco" in data
        assert "tempo_total_focado" in data
        assert "mensagem_feedback" in data

        assert data["tempo_total_focado"] == 210
        assert data["media_nivel_foco"] > 0
        assert isinstance(data["mensagem_feedback"], str)
