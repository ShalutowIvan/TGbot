from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#чтобы быстро написать пишем RKM и жмем ctrl + i + 2 пробела
kb_test = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/menu')
        ],

    ],
    resize_keyboard=True
)

