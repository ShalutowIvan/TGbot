from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from data.config import admins_id
from keyboard.default import kb_menu
from loader import dp
from states import reg
from utils.db_api import table_commands


@dp.message_handler(text='Отмена', state=[reg.food, reg.sleep, reg.toilet])
async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Что дальше?', reply_markup=kb_menu)

#тут мы вводим еду, она должна сохраняться в новую таблицу, в случае если это новый пользователь. Или если это старый пользователь, то добавлять данные в таблицу именно этого пользователя. У меня пока постоянно добавляет новую таблицу, не добавляет данные в нее. Как работает с разными пользователями неизвестно, нужно проверять
@dp.message_handler(text='Указать время приема пищи')
async def bot_register(message: types.Message):

    food = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer(f'Привет\n'
                         f'Введи кусь',
                         reply_markup=food)
    await reg.food.set()



@dp.message_handler(state=reg.food)
async def get_name(message: types.Message, state: FSMContext):
    # answer = message.text
    await state.update_data(food=message.text)
    sleep = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer(f"Сколько спал", reply_markup=sleep)
    await reg.sleep.set()

@dp.message_handler(state=reg.sleep)
async def get_gender(message: types.Message, state: FSMContext):
    await state.update_data(sleep=message.text)
    toilet = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer(f"Ходил в туалет?", reply_markup=toilet)
    await reg.toilet.set()

@dp.message_handler(state=reg.toilet)
async def get_gender(message: types.Message, state: FSMContext):
    await state.update_data(toilet=message.text)
    data = await state.get_data()
    food = data.get('food')
    sleep = int(data.get('sleep'))
    toilet = data.get('toilet')
    await table_commands.add_tables(user_id=message.from_user.id, food=food, sleep=sleep, toilet=toilet)
    #тут все переделать.....
    await state.finish()

@dp.message_handler(text='готово', user_id=admins_id)
async def get_reg(message: types.Message):
    tab = await table_commands.select_tables()

    await message.answer(f"Еда {reg.food}\n"
                         f"Сон {reg.sleep}\n"
                         f"Туалет {reg.toilet}"
                         )




