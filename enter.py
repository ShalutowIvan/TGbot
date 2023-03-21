async def on_startup(dp):
	from utils.notify_admins import onstartup_notify
	await onstartup_notify(dp)#эта функция будет отправлять сообщения всем админам бота, которые мы пропищем в config сообщение о том, что бот запущен

	from utils.set_bot_commands import set_default_commands
	await set_default_commands(dp)

	print("Бот работает!")

if __name__ == '__main__':
	from aiogram import executor
	from handlers import dp

	executor.start_polling(dp, on_startup=on_startup)





