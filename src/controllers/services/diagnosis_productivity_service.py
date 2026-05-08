import random

from src.controllers.interfaces.diagnosis_productivity_interface import (
    DiagnosisProductivityInterface,
)
from src.models.entities.focus_entity import FocusTable
from src.models.repositories.focus_repository import FocusRepository


class DiagnosisProductivityService(DiagnosisProductivityInterface):
    def __init__(self, repository: FocusRepository) -> None:
        self.repository = repository

    async def get_all_focus_registries(self) -> list[FocusTable]:
        return await self.repository.retrieve_focus()

    async def get_average_focus_level(
        self, focus_registries: list[FocusTable]
    ) -> float:
        total_focus_level = [focus.focus_level for focus in focus_registries]
        average_focus_level = sum(total_focus_level) / len(focus_registries)
        return average_focus_level

    async def get_total_focus_time(
        self, focus_registries: list[FocusTable]
    ) -> int:
        total_focus_time = sum(
            focus.duration_minutes for focus in focus_registries
        )
        return total_focus_time

    async def get_comment_about_focus(
        self,
        average_focus_level: float,
    ) -> str:
        high_focus_messages = [
            "Você entrou em modo deep work. Seu cérebro está voando!",
            "Seu foco está afiado como uma katana.",
            "Hoje você desbloqueou o modo produtividade extrema.",
            "Seu nível de concentração está digno de um monge programador.",
            "Você está transformando minutos em resultados reais.",
            "Seu fluxo de produtividade está consistente e poderoso.",
            "Você está em uma maratona mental de alto desempenho.",
            "Seu foco hoje está acima da média. Continue assim!",
            "Menos distrações, mais execução. Excelente ritmo!",
            "Seu estado de flow está forte hoje. Aproveite esse embalo!",
        ]

        low_focus_messages = [
            "Talvez seja hora de reduzir notificações e respirar um pouco.",
            "Seu foco parece cansado hoje. Que tal uma pausa estratégica?",
            "Nem todo dia é produtivo mas todo dia é uma chance de recomeçar.",
            "Seu cérebro pode estar pedindo descanso ou menos multitarefa.",
            "Tente dividir tarefas grandes em pequenas missões.",
            "Ambiente bagunçado, mente bagunçada. Melhor reorganizar",
            "Seu foco oscilou bastante. Menos abas abertas pode ajudar.",
            "Pausas curtas podem recuperar sua energia mental.",
            "Hoje foi mais sobrevivência. Amanhã melhora!",
            "Talvez um café, uma caminhada ou silêncio possam ajudar.",
        ]

        if average_focus_level > 3:
            return random.choice(high_focus_messages)

        return random.choice(low_focus_messages)
