# from asyncpg import UniqueViolationError
#
# from utils.db_api.schemas.tables_users import Tables
#
#
# async def add_tables(user_id: int, food: str, sleep: int, toilet: str):#добавление пользователя, точнее записи в БД
#     try:
#         new_table = Tables(user_id=user_id, food=food, sleep=sleep, toilet=toilet)
#         # new_table.__tablename__ = str(user_id)
#
#         await new_table.create()#тут создали объект класса User
#     except UniqueViolationError:
#         print('Таблица не создана')
#
#
# async def select_tables():#тут мы выделяем все таблицы
#     tab = await Tables.query.gino.all()
#     return tab
#
# # async def select_tables_by_user_id(user_id: int):#тут мы ищем таблицу пользователя по его ИД
# #     tab = await Tables.query.where(Tables.user_id == user_id).gino.first()
# #     return tab
# #
# # async def accept_tables(user_id: int):
# #     tab = await select_tables_by_user_id(user_id)
# #     await tab.update(status='accepted').applay()
#
#
#
#
#
