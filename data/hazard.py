import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase

class Hazard(SqlAlchemyBase):
    __tablename__ = 'hazard'
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)

    