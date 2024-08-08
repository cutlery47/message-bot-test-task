from src.dto.message import MessageDTO, InMessageDTO
from src.exceptions.repository_exceptions import DataNotFoundException, RepositoryException

from typing import List
from datetime import datetime
import pytz
import os

from pymongo.errors import PyMongoError

from motor.motor_asyncio import AsyncIOMotorClient

from loguru import logger


class Repository:

    def __init__(self, mongo_host: str, mongo_port: int):
        self._mongo = AsyncIOMotorClient(mongo_host, mongo_port)
        self._database = self._mongo[os.getenv('MONGO_DATABASE')]
        self._collection = self._database[os.getenv('MONGO_COLLECTION')]

    async def post(self, in_message: InMessageDTO) -> MessageDTO:
        session = await self._mongo.start_session()
        session.start_transaction()

        message = MessageDTO(posted_at=datetime.now(pytz.timezone('Europe/Moscow')).strftime("%d/%m/%Y в %H:%M"),
                             **in_message.model_dump())

        try:
            await self._collection.insert_one(message.model_dump())
            await session.commit_transaction()

        except PyMongoError as exc:
            await session.abort_transaction()
            logger.error(str(exc))
            raise RepositoryException()

        else:
            await session.end_session()
            logger.info("Сообщение успешно добавлено в БД")

        return message

    async def get(self, skip: int, limit: int) -> List[MessageDTO]:
        res = []

        messages = self._collection.find({}).skip(skip * limit).limit(limit)

        async for message in messages:
            res.append(MessageDTO(**message))

        if len(res) == 0:
            raise DataNotFoundException("Сообщения не были найдены")
        else:
            logger.info(f"Получено {len(res)} сообщений из БД")

        return res

    async def delete(self):
        session = await self._mongo.start_session()
        session.start_transaction()

        try:
            await self._collection.delete_many({})
            await session.commit_transaction()

        except PyMongoError as exc:
            await session.abort_transaction()
            logger.error(str(exc))
            raise RepositoryException()

        else:
            await session.end_session()
            logger.info("Все сообщения удалены из БД")
