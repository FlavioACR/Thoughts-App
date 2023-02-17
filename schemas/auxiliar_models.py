# DEPENDENCIES:
# Python
from enum import Enum


class ThougthAndQuestionCategory(Enum):
    '''
    ThougthAndQuestionCategory Class
    
    This class contain a list of the posible topic to make a though and question to the community of the app.
    
    Inheritance:
        Enum Class
    
    Parameters:
    
        Nothing
        
    Attributes:
    
        Variables posibles to choice:
      
            personal   = "Personal"
            work       = "Work"
            deport     = "Deport"
            love       = "Love"
            friendship = "FriendShip"
            familiar   = "Familiar"
            business   = "Business"
            technology = "Technology"
    '''
    personal   = "Personal"
    work       = "Work"
    deport     = "Deport"
    love       = "Love"
    friendship = "FriendShip"
    familiar   = "Familiar"
    business   = "Business"
    technology = "Technology"
