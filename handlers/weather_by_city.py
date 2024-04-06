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
    city = message.text
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=024e2078c2ad10abfde94667edee771d&units=metric&lang=ru"
        weather_data = httpx.get(url=url).json()
        if weather_data["cod"] == 404:
            await message.answer("Такой город не найден...Дай другой город🙃")
            return
        print(weather_data)
        # longitude = weather_data["coord"]["lon"]
        longitude, latitude = weather_data["coord"].values()
        weather = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        feel_like = weather_data["main"]["feels_like"]
        pressure = weather_data["main"]["pressure"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        wind_direction = weather_data["wind"]["deg"]
        clouds_percentage = weather_data["clouds"]["all"]
        sunrise = datetime.fromtimestamp(weather_data["sys"]["sunrise"])
        sunset = datetime.fromtimestamp(weather_data["sys"]["sunset"])
        await message.reply(
            text=f"Город: {city}\n"
                 f"Температура: {temperature} °C\n"
                 f"Как ощущается: {feel_like} °C\n"
                 f"Общее описание: {weather}\n"
                 f"Процент облачности: {clouds_percentage} %\n"
                 f"Скорость ветра: {wind_speed} м/с\n"
                 f"Направление ветра(азимут): {wind_direction}\n"
                 f"Давление: {pressure} Па\n"
                 f"Влажность: {humidity} %\n"
                 f"Широта: {latitude}\n"
                 f"Долгота: {longitude}\n"
                 f"Восход (по Калининградскому времени): {sunrise}\n"
                 f"Закат (по Калининградскому времени): {sunset}\n"
                 f"Восход (по Местному времени): {sunrise}\n"
                 f"Закат (по Местному времени): {sunset}\n",
            reply_markup=main_keyboard()
        )
        await state.clear()
    except Exception as e:
        print(e, type(e), e.args, e)
        await message.answer("😓Ой, что-то пошло не так...Дай другой город😨")


