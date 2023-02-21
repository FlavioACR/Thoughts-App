# Database
from config.database import Base

# SQLalchemy
from sqlalchemy import Column, Integer, String, Float, Date ,ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime

class Questions(Base):
   __tablename__ = "questions"
   
   question_id       = Column(Integer, primary_key=True, index=True, autoincrement=True)
   user_id           = Column(Integer, ForeignKey("users.user_id", ondelete='CASCADE'), nullable=False) 
   question_category = Column(String, nullable=False)
   question_content  = Column(String(255), nullable=False)
   created_at        = Column(Date, nullable=False)
   question_status   = Column(String, nullable=False)
   date_status_update= Column(Date, nullable=False)
   
   
   # Relations
   users_relationship =  relationship("Users", back_populates="questions_relationship")
   #answers_relationship = relationship("Answers", back_populates="questions_relationship")
