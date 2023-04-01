import sqlalchemy
from sqlalchemy import Column, BigInteger, String, sql

from utils.db_api.db_users_config import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'#предали название таблицы
    user_id = Column(BigInteger, primary_key=True)#тут оставили примари кей, так как юзер Ид не может повторяться в колонке юзерИД
    first_name = Column(String(200))
    last_name = Column(String(200))
    user_name = Column(String(50))#если оставить примари кей, то могут быть ошибки если юзер нейм на заполнен
    status = Column(String(30))
    # referal_id = Column(BigInteger)#это для реферальной системы

    query: sql.select#создали переменную для запроса к БД

# далее для взаимодействия с таблицей нужно создать команду. Для этого сделаем отдельный файл в папке db_api