# import sqlalchemy
# from sqlalchemy import Column, BigInteger, String, sql
#
# from utils.db_api.db_users_config import TimedBaseModel
#
#
# class Tables(TimedBaseModel):
#     # from aiogram import types
#     # from loader import dp
#     # @staticmethod
#     # @dp.message_handler(text='Регистрация')
#     # async def regas(message: types.Message):
#     #     __tablename__ = str(message.from_user.id)
#
#     __tablename__ = 1#передали название таблицы
#     user_id = Column(BigInteger, primary_key=True)#тут оставили примари кей, так как юзер Ид не может повторяться в колонке юзерИД
#     food = Column(String(200))
#     sleep = Column(BigInteger)
#     toilet = Column(String(50))
#     # status = Column(String(25))
#     # __tablename__ = user_id
#
#     query: sql.select#создали переменную для запроса к БД
#
# # далее для взаимодействия с таблицей нужно создать команду. Для этого сделаем отдельный файл в папке db_api