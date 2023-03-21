#замена одной клавиатуры на другую, и братно. заменяем нашу клавиатуру на тестовую, в которой будет кнопка для вызова опять же нашего меню, и жмем эту кнопку п возвращаемся обратно, то типа зашли в папку и вышли вернулись обратно
from aiogram import types

from keyboard.default import kb_test
from loader import dp

@dp.message_handler(text='Любой текст')
async def test(message: types.Message):#будет вызываться при написании команды /start
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Тут должен быть какой-то текст', reply_markup=kb_test)

