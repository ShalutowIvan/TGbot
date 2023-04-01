from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Указать еду', callback_data='Еда'),
                                        InlineKeyboardButton(text='Указать время сна', callback_data='Сон'),
                                        InlineKeyboardButton(text='Туалет', callback_data='Туалет')
                                    ]
                                ])


