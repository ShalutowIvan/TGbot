# это файл для теста ДБ
import asyncio

from data import config

from utils.db_api import commands_reg_user as commands
from utils.db_api.db_users_config import db


async def db_test():
    await db.set_bind(config.POSTGRES_URI)#тут устанавливается подключени к ДБ через ссылку
    # await db.gino.drop_all()#удалили все таблицы
    await db.gino.create_all()#заново создаем таблицы
    #создаем пользователей
    await commands.add_user(1, 'Ivan', 'net')
    await commands.add_user(2, 'Marina', 'net')
    await commands.add_user(3, 'Victor', 'net')
    await commands.add_user(4, 'Margo', "Dima")

    users = await commands.select_all_users()#выделили всех пользователей
    print(users)#и вывели их на экран

    count = await commands.count_users()
    print(count)

    user = await commands.select_user(1)
    print(user)

    await commands.update_user_name(2, 'Cat')
    print(user)

    user = await commands.select_user(1)
    print(user)


#запускаем асинхронную функцию
loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())

#при запуске добавляются пользователи. Если пользователь уже есть, то питон выдаст сошибку. Можно использовать для того чтобы убрать повторения регистрации пользователя с помощью обработчика исключений

