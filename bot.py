import asyncio
from aiogram import Bot, Dispatcher

from handlers import other_handlers, population_by_city, population_by_country, weather_by_city


async def main():
    bot = Bot(token="7177588604:AAF3nUVQ08wh3QXzVRzj0fAE4vOOS3W3H3s")
    dp = Dispatcher()
    dp.include_routers(
        weather_by_city.router,
        population_by_city.router,
        population_by_country.router,
        other_handlers.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
