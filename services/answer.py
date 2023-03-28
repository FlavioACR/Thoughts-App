# DEPENDENCIES:
# Python
from typing import Optional, List
from datetime import date
# Pydantic
from pydantic import BaseModel, Field

# From models.py for SQLalchemy:
from models.answer import Answers as AnswerModel
# From schemas.py for Pydantic:
from schemas.answer import Answers, AnswerUpdater

class AnswerService():
    
    def __init__(self, db) -> None:
        self.db = db

    def post_answer(self, answer: Answers):
        new_answer = AnswerModel(**answer.dict())
        self.db.add(new_answer)
        self.db.commit()
        return
    
    def show_answers(self):
        result = self.db.query(AnswerModel).all()
        return result
    
    def get_answer(self, answer_id: int):
        result = self.db.query(AnswerModel).filter(AnswerModel.answer_id == answer_id).first()
        return result
    
    # Return answer fo question_id:
    def get_answer_of_question(self, question_to_response_id: int):
        result = self.db.query(AnswerModel).filter(AnswerModel.question_to_response_id == question_to_response_id).first()
        return result
     
    def update_answer(self, answer_id: int, data_answer_update: AnswerUpdater):
        
        answer_to_update = self.db.query(AnswerModel).filter(AnswerModel.answer_id == answer_id).first()
        
        answer_to_update.response_content = data_answer_update.response_content
        answer_to_update.response_date    = data_answer_update.response_date
        
        self.db.commit()
        return
         
    def delete_answer(self, answer_id: int):
       result = self.db.query(AnswerModel).filter(AnswerModel.answer_id == answer_id).delete()
       self.db.commit()
       
       return
