from pydantic import BaseModel, ConfigDict, Field


class DiagnosisProductivityResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        serialize_by_alias=True,
    )

    average_focus_level: float = Field(
        alias="media_nivel_foco",
    )
    total_focus_time: int = Field(
        alias="tempo_total_focado",
    )
    feedback_message: str = Field(
        alias="mensagem_feedback",
    )
