from ..extentions import ma
from ..controller import AbsModel
from sqlalchemy import BigInteger, Column, Text, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class ItemsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'description', 'rental_period', 'prg_location', 'equipment_type', 'offer_until')

ITEMS_SCHEMA = ItemsSchema(many=True)

class Items(AbsModel):
    __tablename__ = 'Items'

    id = Column(BigInteger, primary_key=True)
    description = Column(Text)
    rental_period = Column(Text)
    prg_location = Column(Text)
    equipment_type = Column(Text)
    offer_until = Column(Date)