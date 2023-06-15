# DEPENDENCIES


from utils.jwt_manager import create_token
# Python
from typing import Optional, List
from datetime import date
# Pydantic
from pydantic import BaseModel, Field
# FastAPI
from fastapi import FastAPI, Request, Response, Form, APIRouter, Depends, Path, Query, status, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
# From apps modules: #   config.py:
from config.database import Session
# From models.py for SQLalchemy:
from models.users import Users as UserModel
# From schemas.py for Pydantic:
from schemas.users import UserBase, UserCreate, User
from services.users import UserService


user_router = APIRouter()

# Plantillas HTML 
template = Jinja2Templates(directory='./templates')

##------------------- CRUD -------------------## 


@user_router.get(path='/signup',
                  response_class=HTMLResponse,
                  status_code=status.HTTP_202_ACCEPTED,
                  summary="Create a User in the App",
                  tags=["Users"])
def signup_user(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})

@user_router.post("/creating_user")
def creating_user(
    username: str = Form(),
    email: str = Form(),
    first_name: str = Form(),
    last_name: str = Form(),
    birth_date: str = Form(),
    gender: str = Form(),
    password: str = Form()
):
    new_user_data = {
        "username": username,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "birth_date": birth_date,
        "gender":gender,
        "password":password
    }

    # Crear una funcion que pueda llamar para ingresar la información del nuevo usuario.
    # Tambien se debe de incluir el agregar automaticamente el ID.
    
    

@user_router.get(path='/login',
                  response_class=HTMLResponse,
                  status_code=status.HTTP_202_ACCEPTED,
                  summary="Page to login a user in the app",
                  tags=["Users"])
def login_user(req: Request):
    return template.TemplateResponse("login.html", {"request": req})

'''
@app.post("/data-processing")
def data_processing(firstname: str = Form(), lastname: str = Form(), username: str = Form(), country: str = Form(), password_user: str = Form()):
  data_user = {
    "firstname": firstname,
    "lastname": lastname,
    "username": username,
    "country": country,
    "password_user": password_user
  }
  db = User(data_user)
  db.create_user()@app.post("/data-processing")
def data_processing(firstname: str = Form(), lastname: str = Form(), username: str = Form(), country: str = Form(), password_user: str = Form()):
  data_user = {
    "firstname": firstname,
    "lastname": lastname,
    "username": username,
    "country": country,
    "password_user": password_user
  }
  db = User(data_user)
  db.create_user()
'''



@user_router.post(path='/sign_up',
                  response_model=User,
                  status_code=status.HTTP_201_CREATED,
                  summary="Sign Up a new user in the app",
                  tags=["users"])
def create_user(user: UserCreate):
    # Necesito cambiar la esctructura para devolver el formulario conectado al html.
    """"
    Create_user:
    
    This path operation register a user in the app
    
    Parameters: 
    
         - Request body parameter
            - user: UserCreate 
    
    Returns a successfull registered message
    
        - message: The user has successfully registered
    """
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "The user has successfully registered"})


@user_router.get(path='/users',
                 response_model=List[User],
                 status_code=status.HTTP_200_OK,
                 summary="Show all the users in the app",
                 tags=["users"])
def read_users():
    """
    Show all user
    
    This path operation show alla the users created in the app
    
    Parameters: 
    
        - Nothing
        
    Returns a list of model User with the informaction of each user:
    
        - user_id   : UUID
        - user_name : str
        - email     : Emailstr
        - first_name: str
        - last_name : str
        - birth_date: date
        - genre     : Genre    
    """
    db = Session()
    users = UserService(db).show_users()
    json_users = jsonable_encoder(users)
    
    return JSONResponse(content=json_users)


@user_router.get(path='/users/{user_id}',
                 response_model=User,    
                 status_code=status.HTTP_200_OK,
                 summary="Get and show a specific user in the app",
                 tags=["users"])
def get_a_user(user_id: int = Path(...,
                                    title="User ID",
                                    description="This is a user ID",
                                    example=1)):
    """
    Get a show a user
    
    This path operation get and show the users created in the app
    
    Parameters: 
    
        - user_ id : str
        
    Returns model User with the informaction of the user:
    
        - user_id   : UUID
        - user_name : str
        - email     : Emailstr
        - first_name: str
        - last_name : str
        - birth_date: datetime
        - genre     : Genre    
    """
    db = Session()
    user = UserService(db).get_user(user_id)

    if not user:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': "User Not Found, Sorry"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(user))

    
## Update a user:
@user_router.put(path='/users/{user_id}',
                 response_model=User,
                 status_code=status.HTTP_200_OK,
                 summary="Update a user information in the app",
                 tags=["users"])
def update_user(user_id: int, new_data_for_user: UserCreate):
    """
    Update a user information
    
    This path operation select a user and update the informations of the user created in the app
    
    Parameters: 
    
        - user_ id :         str
        - new_data_for_user: UserCreate
        
    Returns model User with the informaction of the user:

    Returns a message of the process:
    
        Successful Update:
        
        - message: The User Was been Updated      
    
       No user in the database:
       
       - message: User Not Found, Sorry 
    
    """
    # Mejorarar la estructura con un try and except. <<<<<<<< en el modelo de request eliminar qe se modifique el user_id:
    db = Session()
    user_to_update = UserService(db).get_user(user_id)

    if not user_to_update:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': "User Not Found, Sorry"})
    
    # Here we calls the update services:
    UserService(db).update_user(user_id, new_data_for_user)
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={'message': "The User Was been Updated"})


## Delete a user:
@user_router.delete(path='/users/{user_id}',
                    response_model=User,
                    status_code=status.HTTP_200_OK,
                    summary="Delete a user information in the app",
                    tags=["users"])
def delete_user(user_id: int):
    """
    Delete a user information
    
    This path operation select a user and delete from the database of the app
    
    Parameters: 
    
        - user_ id : str
        
    Returns model User with the informaction of the user:

    Returns a message of the process:
    
        Successful Deleted:
        
        - message: The User Was been Deleted    
    
       No user in the database:
       
       - message: User Not Found, Sorry 
    
    """
    db = Session() 
    # PRUEBA DE NUEVO CON TU MANERA Y EJECUTA: 
   
    user_to_delete: UserModel = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    
    if not user_to_delete:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "User Not Found, Sorry"})
    
    UserService(db).delete_user(user_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "The User Was Been Deleted"})