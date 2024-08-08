from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types.message import Message

from src.keyboard.start_keyboard import StartKeyboard, start_message
from src.message.message import InChatMessage

from dataclasses import asdict
from loguru import logger
import httpx
import os

PROXY_HOST = os.getenv("PROXY_HOST")
PROXY_PORT = os.getenv("PROXY_PORT")

msg_router = Router()

@msg_router.message(CommandStart())
async def handle_start_message(message: Message):
    keyboard = StartKeyboard()
    await message.answer(start_message, reply_markup=keyboard.as_markup())


@msg_router.message(F.text != "/start")
async def handle_post(message: Message):
    keyboard = StartKeyboard()
    chat_message = InChatMessage(sender=message.from_user.username, message=message.text)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url=f"http://{PROXY_HOST}:{PROXY_PORT}/api/v1/messages/",
                                         json=asdict(chat_message))
        except httpx.HTTPError as exc:
            logger.error(str(exc))
            await message.answer("Пизда рулю, все сломалось \U0001F494",
                                 reply_markup=keyboard.as_markup())
            return

    if response.status_code == 200:
        await message.answer("Заебись, добавил сообщение \U0000267F",
                             reply_markup=keyboard.as_markup())
    else:
        logger.error(response.text)
        await message.answer("Чет наебнулось хз \U0001F494",
                             reply_markup=keyboard.as_markup())