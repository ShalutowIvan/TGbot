async def on_startup(dp):#создали асинхронную функцию которая будет запускаться при запуске бота

	import middlewares
	middlewares.setup(dp)

	# from loader import db
	# from utils.db_api.db_gino import on_startup
	# print('Подключение к PostgreSQL')
	# await on_startup(dp)
	#
	# print('Удаление базы данных')
	# await db.gino.drop_all()
	#
	# print('Создание таблиц')
	# await db.gino.create_all()
	# print('Готово')


	from utils.notify_admins import onstartup_notify#импортировали функцию которая отправляет сообщения о запуске бота всем администраторам
	await onstartup_notify(dp)#эта функция будет отправлять сообщения всем админам бота, которые мы пропищем в config сообщение о том, что бот запущен

	from utils.set_bot_commands import set_default_commands#импортируем функцию которая устанавливает команды бота
	await set_default_commands(dp)#запустили ее

	print("Бот работает!")#вывод сообщения в консоль при запуске бота

if __name__ == '__main__':
	from aiogram import executor#импорт executorдля запуска пулинга
	from handlers import dp#импорт диспетчера

	executor.start_polling(dp, on_startup=on_startup)#запуск пулинга





