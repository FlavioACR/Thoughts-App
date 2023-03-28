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
from schemas.answer import Answers, AnswerUpdater
# Services:
from services.answer import AnswerService

answer_router = APIRouter()

@answer_router.post(path='/answer',
                      response_model= Answers,
                      status_code=status.HTTP_201_CREATED,
                      summary="Post a Answer for a Question in the app",
                      tags=["Answer"])
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

@answer_router.get(path='/answers',
                   response_model= List[Answers],
                   status_code=status.HTTP_200_OK,
                   summary="Show all the answers in the app",
                   tags=["Answer"])
def show_answers():
    """"
    Show all Answers:
    
    This path operation show all the "Answers" in the app
    
    Parameters:     
         - Nothing
    
    Returns:

        - List of all the answers in the app
    """
    db = Session()
    all_answer = AnswerService(db).show_answers()
    return all_answer

@answer_router.get(path='/answers/{question_id}',
                   response_model= List[Answers],
                   status_code=status.HTTP_200_OK,
                   summary="Show a specific answers by questions in the app",
                   tags=["Answer"])
def show_question(question_id: int = Path(...,
                                    title="Question ID",
                                    description="Questions ID to select Answers",
                                    example=1)):
    """
    Show a Answer of a Question:
    
    This path operation show a specific answr from a Questions in the app
    
    Parameters: 
    
         - question_id
    
    Returns:

        - The list of answers of the questions id selected and found in the app

    """
    db = Session()
    answer_of_question = AnswerService(db).get_answer_of_question(question_id)
    return answer_of_question
    
@answer_router.put(path='/answer/{answer_id}/update',
                      response_model= Answers,
                      status_code=status.HTTP_200_OK,
                      summary="Update content of a answer in the app",
                      tags=["Answer"])
def update_content_answer(answer_id: int, answer_updated: AnswerUpdater):
    """
    Update Answer Content:
    
    This path operation update the conntent answer of  question in the app
    
    Parameters: 
    
         - answer_id
         - answer_updated: Answer
    
    Returns:
        - message: The content's answer has successfully updated
    """
    db = Session()
    answer_to_update = AnswerService(db).get_answer(answer_id)
    
    if not answer_to_update:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': "Answer Not Found, Sorry"})
    
    AnswerService(db).update_answer(answer_id, answer_updated)

    return JSONResponse(status_code=status.HTTP_200_OK, content={'message': "The Answer Was been Updated"})

    
@answer_router.delete(path='/answers/{answer_id}/delete',
                        response_model= Answers,
                        status_code=status.HTTP_200_OK,
                        summary="Delete an answer of questions in the app",
                        tags=["Answer"])
def delete_question(answer_id: int):
    """
    Delete an Answe of a Question:
    
    This path operation delete an answer of a questions in the app
    
    Parameters: 
    
         - answer_id
    
    Returns:
        - message: The answerr has successfully updated
    """
    db = Session()
    answer_to_delete = AnswerService(db).get_answer(answer_id)
    
    if not answer_to_delete:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': "Answer Not Found, Sorry"})
    
    AnswerService(db).delete_answer(answer_id)
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={'message': "The answer Was been Deleted"})
