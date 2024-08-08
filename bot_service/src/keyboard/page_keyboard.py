from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

class PageKeyboard:

    def __init__(self, prev_page: int | None, next_page: int | None):
        self._builder = InlineKeyboardBuilder()

        left_btn = InlineKeyboardButton(text=f"\U00002B05",
                                        callback_data=f'page {str(prev_page)}') if prev_page else None
        right_btn = InlineKeyboardButton(text=f"\U000027A1",
                                         callback_data=f'page {str(next_page)}') if next_page else None
        revert_btn = InlineKeyboardButton(text=f"На главную", callback_data='start')

        if left_btn is not None:
            self._builder.add(left_btn)

        self._builder.add(revert_btn)

        if right_btn is not None:
            self._builder.add(right_btn)

    def as_markup(self):
        return self._builder.as_markup()


