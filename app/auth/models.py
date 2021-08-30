from ..extentions import ma
from ..controller import AbsModel
from sqlalchemy import BigInteger, Column, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'login', 'password', 'email')

USER_SCHEMA = UsersSchema(many=True)

class Users(AbsModel):
    __tablename__ = 'Users'

    id = Column(BigInteger, primary_key=True)
    login = Column(Text)
    password = Column(Text)
    email = Column(Text)