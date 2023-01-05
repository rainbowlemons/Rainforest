from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from dataclasses import dataclass
from models.base import Base
from models.tags import association_table

@dataclass
class Book(Base):
    id: int
    name: str
    price: float
    author_id: int
    publisher_id: int
    
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    price = Column(Float)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
    publisher_id = Column(Integer, ForeignKey("publishers.id"))
    publisher = relationship("Publisher", back_populates="books")
    tags = relationship("Tag", secondary=association_table, back_populates="books")