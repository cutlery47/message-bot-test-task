from aiogram import Router, F
from aiogram.types import CallbackQuery

from src.keyboard.start_keyboard import StartKeyboard, start_message
from src.keyboard.page_keyboard import PageKeyboard
from src.utils.utils import stringify_messages

from loguru import logger
import httpx
import os

PROXY_HOST = os.getenv("PROXY_HOST")
PROXY_PORT = os.getenv("PROXY_PORT")

MESSAGES_PER_PAGE = 10

clk_router = Router()

@clk_router.callback_query(F.data == "start")
async def handle_callback_start(callback: CallbackQuery):
    keyboard = StartKeyboard()
    await callback.message.answer(start_message, reply_markup=keyboard.as_markup())


@clk_router.callback_query(F.data.startswith("page"))
async def handle_pages(callback: CallbackQuery):
    keyboard = StartKeyboard()
    current_page = int(callback.data.split(" ")[1])

    async with httpx.AsyncClient() as client:
        try:
            messages = await client.get(url=f"http://{PROXY_HOST}:{PROXY_PORT}"
                                            f"/api/v1/messages/?page={current_page}&amount={MESSAGES_PER_PAGE + 1}")
        except httpx.HTTPError as exc:
            logger.error(str(exc))
            await callback.message.answer("Пизда рулю, все сломалось \U0001F494", reply_markup=keyboard.as_markup())
            return

    json_messages = messages.json()
    view_messages = stringify_messages(json_messages)

    prev_page = current_page - 1 if current_page != 1 else None
    next_page = current_page + 1 if len(json_messages) == MESSAGES_PER_PAGE + 1 else None

    page_keyboard = PageKeyboard(prev_page=prev_page, next_page=next_page)

    await callback.message.answer(f"Вот твои сообщения, чед \U0001F52E \n\n" + view_messages,
                                  reply_markup=page_keyboard.as_markup())
