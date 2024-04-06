from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
import json

from keyboards.common_keyboards import main_keyboard
from states import UserStates
from get_data import update_data_countries


router = Router()

try:
    with open("countries_population.json", "r", encoding="utf-8") as file:
        db = json.load(file)
        print("countries loaded done! ALL OK")
except:
    print("countries not loaded done! try get data.")
    update_data_countries()

with open("countries_population.json", "r", encoding="utf-8") as file:
    db: dict = json.load(file)
    # print(db)
    print("countries loaded done! ALL OK")


@router.message(UserStates.user_choice_button, F.text.lower() == "население стран")
async def need_country(message: Message, state: FSMContext):
    await message.answer(
        text="Введи название страны, чтобы узнать население:",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(UserStates.user_choice_city)


@router.message(UserStates.user_choice_city, F.text)
async def get_population(message: Message, state: FSMContext):
    await message.answer(
        text=f"получай: {'; '.join(db.items())}",
        reply_markup=ReplyKeyboardRemove()
    )