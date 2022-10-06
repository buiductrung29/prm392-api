from uuid import UUID
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Date
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

BookCategories = Table(
    "BookCategories",
    Base.metadata,
    Column("BookId", ForeignKey("Book.Id"), primary_key=True),
    Column("CategoryId", ForeignKey("Category.Id"), primary_key=True)
)

BookAuthors = Table(
    "BookAuthors",
    Base.metadata,
    Column("BookId", ForeignKey("Books.Id"), primary_key=True),
    Column("AuthorId", ForeignKey("Authors.Id"), primary_key=True),
)

class Category(Base):
    __tablename__ = "Categories"
    id = Column("Id", Integer, primary_key=True)
    name = Column("Name", String(length=50), nullable=False)
    books = relationship("Book", secondary=BookCategories, back_populates="categories")


class Book(Base):
    __tablename__ = "Books"
    id = Column("Id", UUID, primary_key=True)
    title = Column("Title", String(length=250), nullable=False)
    desc = Column("Description", String, nullable=False)
    short_desc = Column("ShortDescription", String, nullable=False)
    published_date = Column("PublishedDate", Date, nullable=False)
    url = Column("URL", String, nullable=True)
    authors = relationship("Author", secondary=BookAuthors, back_populates="books")
    categories = relationship("Categories", secondary=BookCategories, back_populates="books")

class Author(Base):
    __tablename__ = "Authors"
    id = Column("Id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column("Name", String(length=50), nullable=False)
    books = relationship("Book", secondary=BookAuthors, back_populates="authors")




