import openai
from gtts import gTTS
from aiogram import Bot
from aiogram.types import Message, FSInputFile
from ..kayboards.replay import reply_keyboard
from pycbrf.toolbox import ExchangeRates
import datetime


def currency(val):
    rates = ExchangeRates(datetime.date.today())
    result = rates[val].value
    return str(result)


async def get_voice(message: Message, bot: Bot):
    if message.text == '/start':
        await message.answer('hello my friendo',
                             reply_markup=reply_keyboard)
    elif message.text == 'show the course a dollar':
        await message.answer(currency('USD') + ' dollar')
    elif message.text == 'show the course a euro':
        await message.answer(currency('EUR') + ' euro')
    elif message.text == 'show the course a yen':
        await message.answer(currency('JPY') + ' yen')
    else:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=str(message.text),
            max_tokens=700,
            temperature=0
        )
        audio = gTTS(text=response.choices[0].text, lang="ru", slow=False)
        audio.save('txt.mp3')
        send_audio = FSInputFile(path='txt.mp3')
        await bot.send_voice(message.chat.id, voice=send_audio)

