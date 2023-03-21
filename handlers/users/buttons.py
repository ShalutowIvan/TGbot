#хендлер ловит сообщение 10 и выводит тот текст, который мы прописали. Можно тут писать все что угодно и любые условия. Ну и как обычно пустой хендлер нужно писать именно в конце. В нашем случае его импортировать в файле __init__ нужно последним
from aiogram import types
from loader import dp

@dp.message_handler(text='10')
async def command_button(message: types.Message):#будет вызываться при написании команды /start
    await message.answer(f'ИДИ СПАТЬ')

