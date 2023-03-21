# ссылка на канал для обучения:
# https://www.youtube.com/watch?v=FRUKYZtOaSM&list=PLPELDof3v08efHGT3gVLPCXG5cKRo50Nn&index=2

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

#создаем переменную бота и диспетчера сообщений
bot = Bot(token=)
dp = Dispatcher(bot)


#функция которая срабатывает при старте бота автоматически
async def on_startup(_):
	print("Бот вышел в онлайн")


@dp.message_handler(commands=["start"])
async def fn_start(message: types.Message):
	await message.answer(f'Привет {message.from_user.full_name}')
	print(message.from_user)


# a = message.chat.id#это получение id пользователя
# @dp.message_handler()
# async def get_message(message: types.Message):
# 	a = message.chat.id#это получение id пользователя
# 	# b = types.Message.chat.id#это получение id пользователя? то есть тоже самое, можно писать и так
# 	text1 = f'Привет{message.from_user.full_name}'#теперь тут будет написано привет и имя пользователя
# 	text = 'Ваш текст'
# 	await bot.send_message(a, text = text)

#еще можно сообщения пользователя выводить в консоль в cmd
# print(message.from_user)#это выведется словарь со всеми парамтреами юзера который нам пишем. Можно посмотреть какие параметры есть у этого словаря
# print(message.from_user.full_name)#это выведется полное имя пользователя, который нам пишет


#это функция для запуска пулинга бота. то есть запуск с компа
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

#зависимости файл requirements в нем прописываются версии модулей и библиотек, которые мы подключаем к проекту. Чтобы их выгрузить нужно в консоле в корне проекта написать pip freeze  > requirements.txt. Это нужно для пакетной установки проекта на другом пк или сервере





