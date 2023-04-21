from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='show the course a dollar'
        )
    ],
    [
        KeyboardButton(
            text='show the course a euro'
        )
    ],
    [
        KeyboardButton(
            text='show the course a yen'
        )
    ]
], resize_keyboard=True,)
