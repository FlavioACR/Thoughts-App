# DEPENDENCIES:
# Python
from typing import Optional, List
from datetime import date
# Pydantic
from pydantic import BaseModel, Field
# From models.py for SQLalchemy:
from models.thoughts import Thought as ThoughtModel
# From schemas.py for Pydantic:
from schemas.thoughts import Thought

class ThougthService():
    '''
    ThougthrService Class
    
    This class contain a logic of the path operations for the object thoughts
    
    '''
    def __init__(self, db) -> None:
        self.db = db
    
    # CRUD
    def create_thougth(self, thought: ThoughtModel):
        new_thought = ThoughtModel(**thought.dict())
        
        new_thought.thought_category = str(new_thought.thought_category)
                             
        self.db.add(new_thought)
        self.db.commit()
        return