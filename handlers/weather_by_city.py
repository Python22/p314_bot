from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
import requests
import httpx
import aiohttp
from datetime import datetime
import asyncio

from keyboards.common_keyboards import main_keyboard
from states import UserStates


router = Router()


@router.message(UserStates.user_choice_button, F.text.lower() == "погода")
async def need_weather(message: Message, state: FSMContext):
    await message.answer(
        text="Введи название города, чтобы узнать в нём погоду:",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(UserStates.user_choice_city)


@router.message(UserStates.user_choice_city, F.text)
async def get_weather(message: Message, state: FSMContext):
    pass
