# Before  of create the model we need to create and configurate the database using sqlalchemy:
from config.database import Base
# Import the sqlalchemy's modules to create the ORM models:
from sqlalchemy import Column, Integer, String, Float, Date ,ForeignKey
# To make retlationships:
from sqlalchemy.orm import relationship


# This is the model if for the user table:
class Thought(Base):
   __tablename__ = "thoughts"
   
   thought_id       = Column(Integer, primary_key=True, index=True, autoincrement=True)
   user_id          = Column(Integer, ForeignKey("users.user_id"))
   thought_category = Column(String)
   content          = Column(String)
   created_at       = Column(Date)
   updated_at       = Column(Date)
   
   # This is the first relations betweeen tables in the app, so this variable make a reference to the table
   # where going to make the relations,thi is his parameters: 
   # Firts: Is the name of the class to do the relationship. Second: Is the name of the variable inside of the class related.
   users_relationship =  relationship("Users", back_populates = "thougths_relationship")