from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from dataclasses import dataclass
import bcyrpt

from models.base import Base

@dataclass
class User(Base):
    id: int
    username: str
    password: str
    
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)