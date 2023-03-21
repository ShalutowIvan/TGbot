from gino import Gino
# import sqlalchemy as sa
import sqlalchemy
from sqlalchemy import Column, BigInteger, String
from typing import List
import datetime
db = Gino()


class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sqlalchemy.Table = sqlalchemy.inspect(self.__class__)
        primary_key_columns: List[sqlalchemy.Column] = table.primary_key.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"
#как я понял примерно код выше, мы берем таблицу, генерируем из нее словарь, потом из полученного словаря, мы генерируем кортеж, потом соединеям все значения словаря через пробел в одну строку. Потом возвращается название текущего класса и значения через пробел

#ниже рассмотрим как использовать этот класс. Сначала наследуемся от базового класса.
# class TestModel(BaseModel):
#     __tablename__ = 'testModel'
#     user_id = Column(BigInteger, primary_key=True)
#     name = Column(String(50))
# print(TestModel())

class TimedBaseModel(BaseModel):
    __abstract__ = True

    created_at = db.Column(db.DateTime(True), server_default=db.func.now())#дата когда была создана
    updated_at = db.Column(
        db.DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=db.func.now(),
    )#когда данные в ней будут обновляться
#остановился на 13 мин
# https://www.youtube.com/watch?v=dcbuQMjHj_c&list=PLPELDof3v08efHGT3gVLPCXG5cKRo50Nn&index=10



