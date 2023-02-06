# DEPENDENCIES:
# Python
from typing import Optional, List
from datetime import date
from uuid import UUID
# Pydantic
from pydantic import BaseModel, Field
# From own schemas:
from schemas.auxiliar_models import ThougthAndQuestionCategory as CategoryQuestion

class ThoughtUpdater(BaseModel):
    content           : str = Field(...,
                                    min_length=14,
                                    max_length=256)
    updated_at        : date = Field(...)
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "content": "Put here you content updated",
                "update_at": str(date.today())                
            }
        }
    
class Thought(BaseModel):
    '''
    Thought Class
    
    This class contain the base structure for a thought created in the app.
    
    Inheritance:
        
        BaseModel class from pydantic
                
    Parameters:
        
        Nothing
        
    
    Attributes:

        thougth_id        : UUID
        user_id           : int 
        thougth_category  : Optional[ThougthAndQuestionCategory]
        content           : str
        created_at        : datetime
        updated_at        : Optional[datetime]
              
    '''
    thought_id        : int = Field(...)
    user_id           : int = Field(...)
    # Looking how to create a code to validate the thought category.
    thought_category  : str = Field(...) 
    content           : str = Field(...,
                                    min_length=14,
                                    max_length=256)
    created_at        : date = Field(...) #default=str(date.today()))
    updated_at        : date = Field(...) # Field(..., default=date.now())
    
    class Config:
        orm_mode = True
        
        schema_extra = {
            "example": {
                "thought_id": 1,
                "user_id": 2,
                "thought_category": "Personal",
                "content": "This is the first thought recorder in my app",
                "created_at": str(date.today()),
                "updated_at": str(date.today())
            }
        }

    