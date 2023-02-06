# Before  of create the model we need to create and configurate the database using sqlalchemy:
from config.database import Base
# Import the sqlalchemy's modules to create the ORM models:
from sqlalchemy import Column, Integer, String, Float, Date ,ForeignKey
# To make retlationships:
from sqlalchemy.orm import relationship


# This is the model if for the user table:
class Users(Base):
   __tablename__ = "users"
   
   user_id    = Column(Integer, primary_key=True, index=True, autoincrement=True)
   username   = Column(String, nullable=False)
   email      = Column(String, unique=True, nullable=False)
   first_name = Column(String, nullable=False) 
   last_name  = Column(String, nullable=False)
   birth_date = Column(Date, nullable=False)
   gender     = Column(String, nullable=False)
   password   = Column(String(255), nullable=False)   
   
   thougths_relationship = relationship("Thought", back_populates="users_relationship")
   
