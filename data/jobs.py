import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    topic = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    project = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)
    grade = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    user = orm.relation('User')