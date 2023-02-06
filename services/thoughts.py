# DEPENDENCIES:
# Python
from typing import Optional, List
from datetime import date

# Pydantic
from pydantic import BaseModel, Field

# From models.py for SQLalchemy:
from models.thoughts import Thought as ThoughtModel
# From schemas.py for Pydantic:
from schemas.thoughts import Thought, ThoughtUpdater

class ThoughtService():
    '''
    ThougthrService Class
    
    This class contain a logic of the path operations for the object thoughts
    
    '''
    def __init__(self, db) -> None:
        self.db = db
    
    # CRUD
    def create_thougth(self, thought: ThoughtModel):
        new_thought = ThoughtModel(**thought.dict())                            
        self.db.add(new_thought)
        self.db.commit()
        return
    
    def show_all_thought(self):
        all_thoughts = self.db.query(ThoughtModel).all()
        return all_thoughts
        
    def get_thought(self, thought_id: ThoughtModel):
        thought = self.db.query(ThoughtModel).filter(ThoughtModel.thought_id == thought_id).first()
        
        return thought
    
    def update_thought(self, thought_id: int, new_data_thought: ThoughtUpdater):
        thought_to_update = self.db.query(ThoughtModel).filter(ThoughtModel.thought_id == thought_id).first()
        
        # Data to update:
        thought_to_update.content = new_data_thought.content
        thought_to_update.updated_at = new_data_thought.updated_at
        
        self.db.commit()
        return
        
    def delete_thought(self, thought_id: int):
        self.db.query(ThoughtModel).filter(ThoughtModel.thought_id == thought_id).delete()
        self.db.commit()
        return
    