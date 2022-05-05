import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    topic = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    section = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    grade = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=-1)
    filename = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chel = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')