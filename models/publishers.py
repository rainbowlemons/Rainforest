from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from dataclasses import dataclass
from models.base import Base

@dataclass
class Publisher(Base):
    id: int
    name: str
    
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    books = relationship("Book", back_populates="publisher")