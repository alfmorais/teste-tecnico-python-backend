from sqlalchemy import select

from src.models.entities.focus_entity import FocusTable
from src.views.schemas.v1.focus_registers_schema import FocusDataRequest


class FocusRepository:
    def __init__(self, db):
        self.db = db

    async def create_focus(self, focus: FocusDataRequest) -> FocusTable:
        focus_instance = FocusTable(**focus.model_dump(by_alias=False))
        self.db.add(focus_instance)
        await self.db.commit()
        await self.db.refresh(focus_instance)
        return focus_instance

    async def retrieve_focus(self) -> list[FocusTable]:
        response = await self.db.exec(select(FocusTable))
        return response.scalars().all()
