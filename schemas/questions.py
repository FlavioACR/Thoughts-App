# DEPENDENCIES:
# Python
from typing import Optional, List
from datetime import date
# Pydantic
from pydantic import BaseModel, Field

class Questions(BaseModel):
    
    question_id       : int = Field(...)
    user_id           : int = Field(...)
    question_category : str = Field(...)
    question_content  : str = Field(...,
                                    min_length=25,
                                    max_length=250)
    created_at        : date = Field(...)
    question_status   : str = Field(...)
    date_status_update: date = Field(...)
    
    class Config:
        orm_mode = True
        
        schema_extra = {
            "example": {
                "question_id": 1,
                "user_id": 1,
                "question_category": "Personal",
                "question_content" : "Como podría remplazar un foco?",
                "created_at": "2000-01-20",
                "question_status": "Responsed",
                "date_status_update": "2000-01-20"                
            }
        }
        