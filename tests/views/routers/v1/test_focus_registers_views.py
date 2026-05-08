import pytest


class TestFocusRegistersEndpoint:
    @pytest.mark.asyncio
    async def test_should_create_focus_register_successfully(
        self, client, engine
    ):
        client.app.state.engine = engine

        payload = {
            "nivel_foco": 4,
            "tempo_minutos": 30,
            "comentario": "estudando pytest",
        }

        response = client.post("/registro-foco", json=payload)

        assert response.status_code == 200

        data = response.json()

        assert data["nivel_foco"] == 4
        assert data["tempo_minutos"] == 30
        assert data["comentario"] == "estudando pytest"
        assert "id" in data
        assert "data_criacao" in data
