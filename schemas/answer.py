# DEPENDENCIES:
# Python
from typing import Optional, List
from datetime import date
# Pydantic
from pydantic import BaseModel, Field

class Answers(BaseModel):
    
    answer_id               : int = Field(...)
    question_to_response_id : int = Field(...)
    user_responder_id       : int = Field(...)
    response_content        : str = Field(...,min_length=25,max_length=250)
    response_date           : date = Field(...)
    