# Database
from config.database import Base

# SQLalchemy
from sqlalchemy import Column, Integer, String, Float, Date ,ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime

class Answers(Base):
   __tablename__ = "answers"
   
   answer_id               = Column(Integer, primary_key=True, index=True, autoincrement=True)
   question_to_response_id = Column(Integer, ForeignKey("questions.question_id", ondeleted="CASCADE"), nullable=False)
   user_responder_id       = Column(Interger, nullable=False)
   response_content        = Column(String(255), nullable=False)
   response_date           = Column(Date, nullable=False)
   
   # Relations
   users_relationship =  relationship("Users", back_populates="questions_relationship")
   #questions_relationship = relationship("Questions", back_populates="answers_relationship")
   
