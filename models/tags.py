from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from dataclasses import dataclass
from models.base import Base

association_table = Table(
    "books_tags",
    Base.metadata,
    Column("book_id", ForeignKey("books.id")),
    Column("tag_id", ForeignKey("tags.id")),
)

@dataclass
class Tag(Base):
    id: int
    name: str
    
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    books = relationship("Book", secondary=association_table, back_populates="tags")

