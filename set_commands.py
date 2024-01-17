import asyncio

from aiogram import types

from aiogram import Bot
from config import token

bot = Bot(token, parse_mode="HTML")


async def set_commands():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Меню"),
        types.BotCommand(command="kick_all", description="Исключение пользователя (только для чата)"),
    ])

if __name__ == "__main__":
    asyncio.run(set_commands())