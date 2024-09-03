from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class ProductModel(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    category = Column(String)
    email_fornecedor = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())