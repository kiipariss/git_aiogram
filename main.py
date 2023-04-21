import os
import logging
from gtts import gTTS
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaVideo, BotCommand, BotCommandScopeDefault
import asyncio
from src.handler.basic import get_voice
import openai

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY
openai.Model.list()


async def start_bot():
    API_TOKEN = os.getenv('TOKEN')
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.message.register(get_voice)
    try:
        await dp.start_polling(bot)

    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start_bot())
