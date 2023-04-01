import psycopg2

from utils.db_api.db_users_config import conn

# шпаргалка по psycopg2:
# https://metanit.com/python/database/2.3.php
#в файле postgre.py уже попробовал вставить данные, все получилось. Нужно вставлять кортежем из нужныхх данных

async def add_user(user_id: int, first_name: str, last_name: str, user_name: str):#добавление пользователя, точнее записи в БД
    conn.autocommit = True
    try:
        with conn.cursor() as curs:
            await curs.execute(f"""INSERT INTO users (user_id, first_name, last_name, user_name) VALUES
            ({user_id}, {first_name}, {last_name}, {user_name});""")
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:  # пропишем закрытие соединения с БД
        if conn:
            # cursor.close()#если создаем просто переменную, то нужно закрывать курсор, в случае с менеджером контекста, закрывать его не надо, так как он автоматом закрывает БД
            conn.close()
            print("[INFO] PostgreSQL conncetion closed")



# async def select_user(u_id):
#     conn.autocommit = True
#     with conn.cursor() as curs:
#         await curs.execute(f"""SELECT first_name FROM users WHERE user_id = {u_id};""")
#     res = curs.fetchone()


#
# async def select_all_users():#функция выбирает всех пользователей, которые есть в ДБ
#     users = await User.query.gino.all()
#     return users
#
# async def count_users():#возвращает колво пользователей в Бд
#     count = await db.func.count(User.user_id).gino.scalar()
#     return count#можно использовать и функцию len, так как функция select_pull_users возвращает список, но лучше юзать свою функцию
#
# async def select_user(user_id):#выбирает определенного юзера по его юзерИД
#     user = await User.query.where(User.user_id==user_id).gino.first()#функция поиска по юзер ид
#     return user
#
# async def update_status(user_id, status):#эта функция обновляет юзернейм. ТО есть мы тут меняем update_name
#     user = await select_user(user_id)#тут мы получаем объект юзера
#     await user.update(status=status).apply()

#тут функционал для реферальной системы
#функция для првоерки аргументов при регистрации
# async def check_args(args, user_id: int):
#     #если в аргумент передана пустая строка
#     if args == "":
#         args = "0"
#         return args
#     #если в аргумент переданы не только числа, но и буквы
#     elif not args.isnumeric():#возвращает тру если в строке только цифры
#         args = "0"
#         return args
#     #если в аргумент переданы только числа
#     elif args.isnumeric():
#         #если аргумент такой же как ИД пользователя
#         if int(args) == user_id:
#             args = "0"
#             return args
#         #получаем из базы данных пользователя у которого user_id такой же как переданный аргумент
#         elif await select_user(user_id=int(args)) is None:
#             args = "0"
#             return args
#         #если аргумент прошел все проверки, то возвращаем его
#         else:
#             args = str(args)
#             return args
#     #если что то пошло не так
#     else:
#         args = "0"
#         return args





