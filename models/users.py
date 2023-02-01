# Before  of create the model we need to create and configurate the database using sqlalchemy:
from config.database import Base
# Import the sqlalchemy's modules to create the ORM models:
from sqlalchemy import Column, Integer, String, Float, Date ,ForeignKey
# To make retlationships:
from sqlalchemy.orm import relationship


# This is the model if for the user table:
class Users(Base):
   __tablename__ = "users"
   
   user_id    = Column(Integer, primary_key=True)
   username   = Column(String)
   email      = Column(String, unique=True)
   first_name = Column(String) 
   last_name  = Column(String)
   birth_date = Column(Date)
   gender     = Column(String)
   password   = Column(String)   
