from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Погода")
    kb.button(text="Население стран")
    kb.button(text="Население городов")
    return kb.as_markup(resize_keyboard=True)
