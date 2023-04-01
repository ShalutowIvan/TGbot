from aiogram import types
from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command

from loader import dp
from states import registerT


@dp.message_handler(text='Регистрация')#при полученнии команды /register сработает этот хендлер
async def register(message: types.Message):
    await message.answer('Привет, регистрация началась\nВведите имя пупсика')
    await registerT.name.set()#после команды register выведется текст выше и сработает состояние

@dp.message_handler(state=registerT.name)#теперь мы ловим это состояние, которое было выше, все что ввели выше, все сюда попадает
async def state1(message: types.Message, state: FSMContext):
    answer = message.text#тут мы сохранили текст который прислал пользователь
    await state.update_data(name=answer)#в переменную мы записли текст из ответа пользователя, а точнее в словарь добавили элемент по ключу test1 и значением answer
    await message.answer(f'Какой пол ребенка?')#можно дописать и имя и спросить сколько лет
    await registerT.gender.set()#тут включается второе состояние и пользователь когда что то введет, то оно считается

@dp.message_handler(state=registerT.gender)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text#тут мы сохранили текст который прислал пользователь
    await state.update_data(gender=answer)#в переменную мы записли текст из ответа пользователя, а точнее в словарь добавили элемент по ключу test1 и значением answer
    await message.answer(f'Введите дату рождения')#можно дописать и имя и спросить сколько лет
    await registerT.date_of_birth.set()#тут включается второе состояние и пользователь когда что то введет, то оно считается


@dp.message_handler(state=registerT.date_of_birth)#ловим второе состояние
async def state3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(date_of_birth=answer)#добавили еще одно значение в словарь с другим ключом
    data = await state.get_data()#здесь мы в переменную записали итоговый словарь
    name = data.get('name')
    gender = data.get('gender')
    date_of_birth = data.get('date_of_birth')
    await message.answer('Регистрация успешно завершена\n'
                         f'Имя ребенка {name}\n'
                         f'У вас {gender}\n'
                         f'Родился {date_of_birth}')
    await state.finish()

#в машине состояний не работают инлайн кнопки










