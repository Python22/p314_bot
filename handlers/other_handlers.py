from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.common_keyboards import main_keyboard
from states import UserStates


router = Router()


@router.message(Command("start"))               # /start
async def start(message: Message, state: FSMContext):
    await message.answer(
        text="Выбери один из пунктов: ",
        reply_markup=main_keyboard()
    )
    await state.set_state(UserStates.user_choice_button)
