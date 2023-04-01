#тут опросник админов идет

from aiogram import Dispatcher
from data.config import admins_id

async def onstartup_notify(dp: Dispatcher):
	for adm in admins_id:
		await dp.bot.send_message(chat_id=adm, text="Бот запущен")



