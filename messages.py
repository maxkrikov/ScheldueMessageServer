import asyncio

from aiogram import Bot
from config import token
from base import PostgresConnector

bot = Bot(token, parse_mode="HTML")


async def send_message(id: str):
    all_element = PostgresConnector().get_data_by_id(int(id))
    if not all_element:
        return None
    chatId = all_element[1]
    text = all_element[2]

    if all_element[4]:
        await bot.send_photo(chatId, photo=all_element[4], caption=text)
    else:
        await bot.send_message(chatId, text)
    await bot.session.close()

    PostgresConnector().delete_data_by_id(int(id))
