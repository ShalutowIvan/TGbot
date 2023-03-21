#тут опросник админов идет
import logging#это библиотека логики

from aiogram import Dispatcher
from data.config import admins_id

async def onstartup_notify(dp: Dispatcher):
	for adm in admins_id:
		try:
			text = "Бот запущен"
			await dp.bot.send_message(chat_id=adm, text=text)
		except Exception as err:
			logging.exception(err)#сюда будут попадать ошибки



