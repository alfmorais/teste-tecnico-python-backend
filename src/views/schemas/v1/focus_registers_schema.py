from datetime import datetime

from pydantic import BaseModel, Field


class FocusDataRequest(BaseModel):
    focus_level: int = Field(
        ...,
        ge=1,
        le=5,
        description="Focus level from 1 (very distracted) to 5 (flow state).",
        alias="nivel_foco",
    )
    duration_minutes: int = Field(
        ...,
        gt=0,
        description="Duration of the focus session in minutes.",
        alias="tempo_minutos",
    )
    comment: str = Field(
        ...,
        min_length=1,
        description="Description of the activity performed.",
        alias="comentario",
    )


class FocusDataResponse(BaseModel):
    model_config = {
        "populate_by_name": True,
        "serialize_by_alias": True,
    }

    id: int = Field(
        ...,
        description="Unique identifier of the focus register.",
    )
    focus_level: int = Field(
        ...,
        ge=1,
        le=5,
        description="Focus level from 1 (very distracted) to 5 (flow state).",
        alias="nivel_foco",
    )
    duration_minutes: int = Field(
        ...,
        gt=0,
        description="Duration of the focus session in minutes.",
        alias="tempo_minutos",
    )
    comment: str = Field(
        ...,
        min_length=1,
        description="Description of the activity performed.",
        alias="comentario",
    )
    created_at: datetime = Field(
        ...,
        description="Date and time when the focus register was created.",
        alias="data_criacao",
    )
