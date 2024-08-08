from aiogram import Bot, Dispatcher
import asyncio
import os

from src.handlers.message_handlers import msg_router
from src.handlers.callback_handlers import clk_router

TOKEN = os.getenv('BOT_TOKEN')

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(msg_router)
    dp.include_router(clk_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())





