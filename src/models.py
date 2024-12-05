from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

from src.database.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    quantity = Column(Integer, default=0)

    category_id = Column(
        Integer,
        ForeignKey("categories.id", ondelete="CASCADE")
    )
    category = relationship("Category", back_populates="products")


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)

    products = relationship(
        "Product", back_populates="category", cascade="all, delete-orphan"
    )
