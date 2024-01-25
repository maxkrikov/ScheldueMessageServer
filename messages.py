import asyncio
import json

from aiogram import Bot
from config import token
from base import PostgresConnector
from aiogram import types

bot = Bot(token)


async def send_message(id: str):
    all_element = PostgresConnector().get_data_by_id(int(id))
    if not all_element:
        return None
    chatId = all_element[1]
    text = all_element[2]
    entity = []

    if all_element[5]:
        entitys = json.loads(all_element[5])

        for en in entitys:
            entity.append(types.MessageEntity(type=en['type'], offset=int(en['offset']),
                                              length=int(en['length']), url=en['url'],
                                              text=en['text']))
    if all_element[4]:
        await bot.send_photo(chatId, photo=all_element[4], caption=text, caption_entities=entity)
    else:
        await bot.send_message(chatId, text, entities=entity)
    await bot.session.close()
