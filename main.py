""" импорт asyncio """
import asyncio
from aiogram import Bot, Dispatcher
from handlers import include_router

bot = Bot(token="7132743665:AAHmq7AFNRDRrWbG-Lz8vn9O2B8A84gmCY0")
dp = Dispatcher()

async def main():
    """ подключение роутеров и запуск бота """
    include_router(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
