from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_message = "Добро пожаловать в хуебот \U0001F450 \n\n" \
                "Для получения доступных сообщений въеби \"Получить сообщения\" \U00002705 \n\n" \
                "Для отправки нового сообщения просто высри что-нибудь в чат \U0001F6BC"

class StartKeyboard:

    def __init__(self):
        get_btn = InlineKeyboardButton(text=f"Получить сообщения \U00002709", callback_data='page 1')
        self._start_markup = InlineKeyboardMarkup(inline_keyboard=[[get_btn]])

    def as_markup(self):
        return self._start_markup
