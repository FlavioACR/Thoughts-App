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
# from fastapi import HTTPException
# From apps modules:
#   config.py:
from config.database import Session
# From models.py for SQLalchemy:
from models.thoughts import Thought as ThoughtModel
# From schemas.py for Pydantic:
from schemas.thoughts import Thought
from services.thoughts import ThougthService


thought_router = APIRouter()

# CRUD:
@thought_router.post(path='/create/though',
                  response_model=Thought,
                  status_code=status.HTTP_201_CREATED,
                  summary="Create a thougth from a user in the app",
                  tags=["Thought"])
def create_user(user: Thought):
    """"
    T:
    
    This path operation register a user in the app
    
    Parameters: 
    
         - Request body parameter
            - user: UserCreate 
    
    Returns a successfull registered message
    
        - message: The user has successfully registered
    """
    db = Session()
    ThougthService(db).create_thougth(user)
    return JSONResponse(status_code=201, content={"message": "The thought has successfully registered"})