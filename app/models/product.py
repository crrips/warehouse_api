from sqlalchemy import Column, Integer, String, Float, ForeignKey
from models.base import Base


class Product(Base):
    def __init__(self, name, description, price, amount):
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount
        
    __tablename__ = 'product'
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)
    amount = Column(Integer, nullable=False)
    