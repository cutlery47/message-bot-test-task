from src.repository.repository import Repository
from src.dto.message import InMessageDTO, MessageDTO

from typing import List

class Service:

    def __init__(self, repo: Repository):
        self._repo = repo

    async def post(self, in_message: InMessageDTO):
        await self._repo.post(in_message=in_message)

    async def get(self, page: int, amount: int) -> List[MessageDTO]:
        return await self._repo.get(skip=page - 1, limit=amount)
