import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Example(SqlAlchemyBase):
    __tablename__ = 'example'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    value = sqlalchemy.Column(sqlalchemy.Integer)
