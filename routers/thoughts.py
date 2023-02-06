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
from schemas.thoughts import Thought, ThoughtUpdater
from services.thoughts import ThoughtService


thought_router = APIRouter()

# CRUD:
@thought_router.post(path='/create/though',
                    response_model=Thought,
                    status_code=status.HTTP_201_CREATED,
                    summary="Create a thougth from a user in the app",
                    tags=["Thought"])
def create_thought(thought: Thought):
    """"
    Create a Thought:
    
    This path operation create and record a "Thought" from a user in the app
    
    Parameters: 
    
         - Request body parameter
            - thought: Thought 
    
    Returns a successfull registered message
    
        - message: The thought has successfully registered
    """
    db = Session()
    ThoughtService(db).create_thougth(thought)
    return JSONResponse(status_code=201, content={"message": "The thought has successfully registered"})

@thought_router.get(path='/thoughts',
                     response_model=List[Thought],
                     status_code=status.HTTP_200_OK,
                     summary="Show all the thougths from a user in the app",
                     tags=["Thought"])
def show_thoughts():
    """"
    Show all Thought:
    
    This path operation show all the "Thoughts" in the app
    
    Parameters: 
    
         - Nothing
    
    Returns:
    
        - List of all the thoughts in the app
    """
    db = Session()
    all_thoughts = ThoughtService(db).show_all_thought()
    return all_thoughts

@thought_router.get(path='/thoughts/{thought_id}',
                     response_model=Thought,
                     status_code=status.HTTP_200_OK,
                     summary="Show a specific thought in the app",
                     tags=["Thought"])
def show_thoughts(thought_id: int = Path(...,
                                    title="Thougth ID",
                                    description="This is a thought ID",
                                    example=1)):
    """"
    Show all Thought:
    
    This path operation show all the "Thoughts" in the app
    
    Parameters: 
    
         - Nothing
    
    Returns:
    
        - List of all the thoughts in the app
    """
    db = Session()
    all_thoughts = ThoughtService(db).get_thought(thought_id)
    return all_thoughts

@thought_router.put(path='/thoughts/{thought_id}',
                    response_model=Thought,
                    status_code=status.HTTP_200_OK,
                    summary="Update a thought in the app",
                    tags=["Thought"])
def update_thought(thought_id: int, new_data_though: ThoughtUpdater):
    db = Session()
    thought_to_update = ThoughtService(db).get_thought(thought_id)
    
    if not thought_to_update:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': "Thought Not Found, Sorry"})
    
    ThoughtService(db).update_thought(thought_id, new_data_though)
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={'message': "The Thought Was been Updated"})

@thought_router.delete(path='/thoughts/{thought_id}',
                       response_model=Thought,
                       status_code=status.HTTP_200_OK,
                       summary="Update a thought in the app",
                       tags=["Thought"])
def delete_thought(thought_id: int):
    db = Session()
    thought_to_update = ThoughtService(db).get_thought(thought_id)
    
    if not thought_to_update:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': "Thought Not Found, Sorry"})
    
    ThoughtService(db).delete_thought(thought_id)
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={'message': "The Thought Was been Updated"})
