# DEPENDENCIES:
# Python
from typing import Optional, List
from datetime import date
# Pydantic
from pydantic import BaseModel, Field

# From models.py for SQLalchemy:
from models.questions import Questions as QuestionsModel
# From schemas.py for Pydantic:
from schemas.questions import Questions

class QuestionService():
    
    def __init__(self, db) -> None:
        self.db = db
    
    def create_question(self, question: Questions):
        new_question = QuestionsModel(**question.dict())
        self.db.add(new_question)
        self.db.commit()
        return
    
    def show_question(self):
        result = self.db.query(QuestionsModel).all()
        return result
    
    def get_question(self, question_id: int):
        result = self.db.query(QuestionsModel).filter(QuestionsModel.question_id == question_id).first()
        return result
    
    def update_question(self, question_id: int, question_updated: Questions):
        
        question_to_update = self.db.query(QuestionsModel).filter(QuestionsModel.question_id == question_id).first()
        
        question_to_update.question_content = question_updated.question_content
        question_to_update.question_status = question_updated.question_status
                
        self.db.commit()
        return
    
    def delete_question(self, question_id: int):
       self.db.query(QuestionsModel).filter(QuestionsModel.question_id == question_id).delete()
       self.db.commit()
       return
