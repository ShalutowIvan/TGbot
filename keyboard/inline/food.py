from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboard.inline import ikb_menu

ikb_food = InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Указать время приема пищи', callback_data='1'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Рацион', callback_data='2'),
                                        InlineKeyboardButton(text='Отчеты', callback_data='3')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад', callback_data='Назад')
                                    ]
# , reply_markup=ikb_menu
                                ])


