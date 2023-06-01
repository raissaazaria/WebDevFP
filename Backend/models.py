from sqlalchemy import Boolean, Column, Integer, String, UniqueConstraint, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.orm import Relationship
from database import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    disabled = Column(Boolean, default=True)
    
    UniqueConstraint("email", name="uq_user_email")
    PrimaryKeyConstraint("id", name="pk_user_id")
    
class seller(Base):
    __tablename__ = "seller"
    
    user_id = Column(Integer, ForeignKey("User.id") )
    product_id = Column(Integer, unique = True) 
    Name = Column(String)
    Quantity = Column(int)
    Status = Column(String)
    
class Purchase(Base):
    __tablename__ = "seller"
    
    user_id = Column(Integer, ForeignKey("User.id") )
    purchase_id = Column(Integer, unique = True) 
    Name = Column(String)
    Quantity = Column(int)
    Status = Column(String)
