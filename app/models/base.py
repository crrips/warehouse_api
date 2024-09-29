from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base_declarative = declarative_base()


class Base(Base_declarative):
    __abstract__ = True
    
    __tablename__ = 'base'
    id = Column(Integer, primary_key=True, index=True)
