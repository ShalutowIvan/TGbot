from aiogram import types
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=3, key='/start')
@dp.message_handler(text='/start')#теперь тут будет подключен фильтр
async def command_start(message: types.Message):#будет вызываться при написании команды /start
    await message.answer(f'Привет {message.from_user.full_name}!')

