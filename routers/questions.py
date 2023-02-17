# DEPENDENCIES:
# Python
from typing import Optional, List
from datetime import date
# Pydantic
from pydantic import BaseModel, Field
# FastAPI
from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder
# Database
from config.database import Session
# From models.py for SQLalchemy:
from models.questions import Questions as QuestionsModel
# From schemas.py for Pydantic:
from schemas.questions import Questions
# Service
from services.questions import QuestionService

question_router = APIRouter()

@question_router.post(path='/create/question',
                      response_model= Questions,
                      status_code=status.HTTP_201_CREATED,
                      summary="create a new Question in the app",
                      tags=["Question"])
def create_question(question: Questions):
    """"
    Create_user:
    
    This path operation register a user in the app
    
    Parameters: 
    
         - Request body parameter
            - user: UserCreate 
    
    Returns a successfull registered message
    
        - message: The user has successfully registered
    """
    db = Session()
    QuestionService(db).create_question(question)
    return JSONResponse(status_code=201, content={"message": "The Question has successfully created"})
