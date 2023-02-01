# DEPENDENCIES:
# Python
from typing import Optional, List
from datetime import date
# Pydantic
from pydantic import BaseModel, Field

# From models.py for SQLalchemy:
from models.users import Users as UserModel
# From schemas.py for Pydantic:
from schemas.users import UserBase, UserCreate, User

class UserService():
    '''
    UserService Class
    
    This class contain a logic of the path operations for the object users
    
    '''
    def __init__(self, db) -> None:
        self.db = db
    
    def create_user(self, user: UserCreate):
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return

    def show_users(self):
        result = self.db.query(UserModel).all()
        return result
    
    def get_user(self, user_id: int):
        result = self.db.query(UserModel).filter(UserModel.user_id == user_id).first()
        return result
    
    def update_user(self, user_id: int, data_new_user: UserCreate):
        user_to_update = self.db.query(UserModel).filter(UserModel.user_id == user_id).first()
        
        user_to_update.username = data_new_user.username
        user_to_update.email    = data_new_user.email
        user_to_update.first_name = data_new_user.first_name 
        user_to_update.last_name = data_new_user.last_name
        user_to_update.birth_date = data_new_user.birth_date 
        user_to_update.gender = data_new_user.gender
        user_to_update.password = data_new_user.password
        
        self.db.commit()
        return
         
    def delete_user(self, user_id: int):
       self.db.query(UserModel).filter(UserModel.user_id == user_id).delete()
       self.db.commit()
       return
