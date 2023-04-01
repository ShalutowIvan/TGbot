#новый файл для старта с регистрацией пользователя по профилю из телеги
from aiogram import types
from handlers.menu import menu
from loader import dp
from utils.db_api import commands_reg_user as commands

@dp.message_handler(text='/start')
async def command_start(message: types.Message):

    await menu(message)
    # try:
    await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                user_name=message.from_user.username)
    await message.answer('Ты успешно зарегистрировался')

        # <b>жирный текст</b>
        # <i>курсив</i>
        #<code>на текст можно будет нажать и он скопируется</code>
        #<s>зачеркнутый текст</s>
        #<u>подчеркнутый текст</u>
        #<a href='Ссылка'>текст ссылки</a>#если передать не ссылку, то текст будет обычным
        #все команды пишутся в строках в питоне

    # except Exception:
    #     with conn.cursor() as curs:
	# curs.execute(#тут мы пишем sql запрос для создания таблицы с нужными нам полями.
	# 	"""SELECT nick_name FROM users WHERE first_name = 'Vasia';"""
	# )
	# print(curs.fetchone())#тут вывели только поле ник Васи в виде кортежа


# @dp.message_handler(text='/profile')
# async def get_unban(message: types.Message):
#     user = await commands.select_user(message.from_user.id)
#     await message.answer(f'ID - {user.user_id}\n'
#                          f'имя - {user.first_name}\n'
#                          f'фамилия - {user.last_name}\n'
#                          f'ник в телеграм - {user.user_name}\n'
#                          f'статус в базе - {user.status}')




