from sqlalchemy import Column, Integer, String, Float, ForeignKey
from models.base import Base


class OrderItem(Base):
    def __init__(self, order_id, product_id, product_amount):
        self.order_id = order_id
        self.product_id = product_id
        self.product_amount = product_amount
    
    __tablename__ = 'order_item'
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    product_amount = Column(Integer, nullable=False)
    