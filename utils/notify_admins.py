#тут опросник админов идет
import logging

from aiogram import Dispatcher

from data.config import admin_id

async def onstartup_notify(dp: Dispatcher):
	for adm in admins_id:
		try:
			text = "Бот запущен"
			dp.bot.send_message(chat_id=adm, text=text)
		except Exception as err:
			logging.exception(err)



