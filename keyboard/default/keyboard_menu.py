from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#чтобы быстро написать пишем RKM и жмем ctrl + i + 2 пробела
kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Регистрация'),
            KeyboardButton(text='11')
        ],
        [
            KeyboardButton(text='100'),
        ],
        [
            KeyboardButton(text='Инлайн меню'),
            KeyboardButton(text='Любой текст'),
            KeyboardButton(text='Лайк')
        ]

    ],
    resize_keyboard=True
)

