from src.service.service import Service
from src.dto.message import InMessageDTO

from fastapi import APIRouter

from loguru import logger

class Controller:

    def __init__(self, service: Service):
        self._service = service
        self._router = APIRouter(prefix="/api/v1/messages")
        self._set_routes()

    def get_routes(self):
        return self._router

    def _set_routes(self):

        @self._router.get("/")
        async def get_messages(page: int, amount: int):
            logger.info("Получен запрос на получение сообщений")
            return await self._service.get(page=page, amount=amount)

        @self._router.post("/")
        async def post_message(in_message: InMessageDTO):
            logger.info("Получен запрос на добавление сообщения")
            await self._service.post(in_message)
            return "Успешно"
