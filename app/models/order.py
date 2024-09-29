from sqlalchemy import Column, Integer, String, Float, ForeignKey
from models.base import Base
from enum import Enum


class OrderStatus(Enum):
    IN_PROCESS = "in process"
    SENT = "sent"
    DELIVERED = "delivered"


class Order(Base):
    def __init__(self, date_created, status):
        self.date_created = date_created
        self.status = status
    
    __tablename__ = 'order'
    date_created = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)
    