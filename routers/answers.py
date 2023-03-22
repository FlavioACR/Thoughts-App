# DEPENDENCIES:
# Python
from typing import Optional, List
from datetime import date
# Pydantic
from pydantic import BaseModel, Field
# # FastAPI
from fastapi import APIRouter
from fastapi import Depends, Path, Query 
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder
# Database
from config.database import Session
# From models.py for SQLalchemy:
from models.answer import Answers as AnswerModel
# From schemas.py for Pydantic:
from schemas.answer import Answers
# Services:
from services.answer import AnswerService

answer_router = APIRouter()

@answer_router.post(path='/answer',
                      response_model= Answers,
                      status_code=status.HTTP_201_CREATED,
                      summary="Post a Answer for a Question in the app",
                      tags=["Asnwer"])
def post_answer(answer: Answers):
    """"
    Post a Answer:
    
    This path operation post an answer for a question in the app
    
    Parameters: 
    
         - Request body parameter
            - question: Answer
    
    Returns a successfull registered message
    
        - message: The answer has successfully posted
    """
    db = Session()
    AnswerService(db).post_answer(answer)
    return JSONResponse(status_code=201, content={"message": "The Answer has successfully posted"})

# # # @question_router.get(path='/questions',
# #                       response_model= List[Questions],
# #                       status_code=status.HTTP_200_OK,
# #                       summary="Show all the questions in the app",
# #                       tags=["Question"])
# # def show_questions():
# #     """"
# #     Show all Questions:
    
# #     This path operation show all the "Questions" in the app
    
# #     Parameters: 
    
# #          - Nothing
    
# #     Returns:

# #         - List of all the questions in the app
# #     """
# #     db = Session()
# #     all_questions = QuestionService(db).show_question()
# #     return all_questions

# # @question_router.get(path='/questions/{question_id}',
# #                       response_model= Questions,
# #                       status_code=status.HTTP_200_OK,
# #                       summary="Show a specific questions in the app",
# #                       tags=["Question"])
# # def show_question(question_id: int = Path(...,
# #                                     title="Question ID",
# #                                     description="This is a questions ID",
# #                                     example=1)):
# #     """
# #     Show a Question:
    
# #     This path operation show a specific Questions in the app
    
# #     Parameters: 
    
# #          - question_id
    
# #     Returns:

# #         - The basic information from the questions found in the app

# #     """
# #     db = Session()
# #     question = QuestionService(db).get_question(question_id)
# #     return question
    
# # @question_router.put(path='/questions/{question_id}',
# #                       response_model= Questions,
# #                       status_code=status.HTTP_200_OK,
# #                       summary="Update status of questions in the app",
# #                       tags=["Question"])
# # def update_status_question(question_id: int, question_updated: Questions):
# #     """
# #     Update Question:
    
# #     This path operation update a the question text or the status of the question in the app
    
# #     Parameters: 
    
# #          - question_id
# #          - question_updated: Questions
    
# #     Returns:
# #         - message: The questions has successfully updated
# #     """
# #     db = Session()
# #     question_to_update = QuestionService(db).get_question(question_id)
    
# #     if not question_to_update:
# #         return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': "Questions Not Found, Sorry"})
    
# #     QuestionService(db).update_question(question_id, question_updated)

# #     return JSONResponse(status_code=status.HTTP_200_OK, content={'message': "The Questions Was been Updated"})

    
# # @question_router.delete(path='/questions/{question_id}',
# #                         response_model= Questions,
# #                         status_code=status.HTTP_200_OK,
# #                         summary="Delete status of questions in the app",
# #                         tags=["Question"])
# # def delete_question(question_id: int, question_updated: Questions):
# #     """
# #     Delete Question:
    
# #     This path operation delete a questions in the app
    
# #     Parameters: 
    
# #          - question_id
    
# #     Returns:
# #         - message: The questions has successfully updated
# #     """
# #     db = Session()
# #     question_to_update = QuestionService(db).get_question(question_id)
    
# #     if not question_to_update:
# #         return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': "Questions Not Found, Sorry"})
    
# #     QuestionService(db).delete_question(question_id)
    
# #     return JSONResponse(status_code=status.HTTP_200_OK, content={'message': "The Questions Was been Deleted"})
