import asyncio
from aiogram import Bot, Dispatcher


async def main():
    bot = Bot(token="7177588604:AAF3nUVQ08wh3QXzVRzj0fAE4vOOS3W3H3s")
    dp = Dispatcher()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
