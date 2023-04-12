# DEPENDENCIES:
# Python
from typing import Optional, List
from datetime import date
# Pydantic
from pydantic import BaseModel, Field


# UserBase    : user_id, username, first_name, last_name, birth_date, gender 
class UserBase(BaseModel):
    user_id   : int = Field(...)
    username  : str = Field(...,
                            min_length=3,
                            max_length=15)
    first_name: str = Field(...,
                            min_length=1,
                            max_length=50)
    last_name : str = Field(...,
                            min_length=1,
                            max_length=50)
    birth_date: Optional[date] = Field(default=None)
    gender    : str = Field(...)
    
# UserPassword: password
class UserPassword(BaseModel):
    email     : str = Field(...)    

# UserEmail   : email
class UserEmail(BaseModel):
    password: str = Field(...,
                          min_length=5,
                          max_length=25)

# UserLogin   : email, password.
class UserLogin(UserPassword, UserEmail):
    pass
    
# User        : user_id, username, first_name, last_name, birth_date, gender, email.
class User(UserBase, UserEmail):
    pass
    
# UserCreate  : user_id, username, first_name, last_name, birth_date, gender, email, password.
class UserCreate(User, UserLogin):
    pass


# class UserBase(BaseModel):
#     # Pendiente de cambiar al valor de ;Gender, Email: talves improtar el GEnder Class:
#     '''
#     User Base Class 
    
#     This class contain all the base attributes to response but don't 
#     inclue dthe password.
    
#     Inheritance:
        
#         #Gender from auxiliar_models.py
        
#     Parameters:
    
        
#     Attributes:
        
#         user_id          : int
#         username         : str 
#         email            : str #EmailStr
#         first_name       : str 
#         last_name        : str 
#         birth_date       : date
#         gender           : str #Gender 

#     '''
#     user_id   : int = Field(...)
#     username  : str = Field(...,
#                             min_length=3,
#                             max_length=15)
#     email     : str = Field(...)
#     first_name: str = Field(...,
#                             min_length=1,
#                             max_length=50)
#     last_name : str = Field(...,
#                             min_length=1,
#                             max_length=50)
#     birth_date: Optional[date] = Field(default=None)
#     gender    : str = Field(...)

# class UserCreate(UserBase):
#     # This pydatic model has all the attributes + the password attribute:
#     '''
#     UserRegister Class
    
#     This class contain all the attributes a user in the app.
    
#     Inheritance:
        
#         UserBase
#         UserLogin.password 

#     Parameters:

#         UserBase  Class
#         UserLogin Class
        
        
#     Attributes:
#         All the attributes are inherited:
    
#         UserBase inherited attributes:
            
#             UserID.user_id : UUID
#             username         : str 
#             email            : EmailStr
#             first_name       : str 
#             last_name        : str 
#             birth_date       : date
#             gender           : Gender

#         UserLogin inherited attributes:
#             UserLogin.password       : str        
#     '''
#     password: str = Field(...,
#                           min_length=5,
#                           max_length=25)

    

# class User(UserBase):
#     # This Class has only the base attributes:
#     class Config:
#         orm_mode = True
        
#         schema_extra = {
#             "example": {
#                 "user_id": 1,
#                 "username": "Usuario1",
#                 "email": "usuario@gmail.com",
#                 "first_name": "Usuario",
#                 "last_name": "Apellido",
#                 "birth_date": "2000-01-20",
#                 "gender": "hombre"
#             }
#         }
