from abc import ABC, abstractmethod

from pydantic import BaseModel


class BaseController[TRequest: BaseModel, TResponse](ABC):
    @abstractmethod
    async def handle(self, data: TRequest) -> TResponse:
        pass
