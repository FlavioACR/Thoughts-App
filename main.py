# DEPENDENCYS:
# Python
from typing import Optional, List
from datetime import date
# Pydantic
from pydantic import BaseModel, Field
# FastAPI
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

#from middlewares.error_handler import ErrorHandler
    #from routers.users import movie_router
    #from routers.users import user_router

# routers/:
from routers.users import user_router
from routers.thoughts import thought_router
from routers.questions import question_router
from routers.answers import answer_router

app = FastAPI()
app.title = "My Thoughts APP with FastAPI"
app.version = "0.0.1"

# Plantillas HTML
template = Jinja2Templates(directory='./templates')

# Declaración de la carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

#app.add_middleware(ErrorHandler)


Base.metadata.create_all(bind=engine)

# Principal base template this is only to create the SuperTemplate:
@app.get(
    path='/',
    status_code=status.HTTP_200_OK,
    summary="Home's app and Hello World",
    tags=['home'])
def home_page(request: Request):
    '''
    Home's app & Hello World FastAPI 

    This path operation say hellow to everybody user in the app

    Parameters: Nothing
    
    Returns   : A json with the greeting information
    '''
    return template.TemplateResponse('welcome_page.html', {"request": request})



# This is the pathoperations for the index:
# @app.get(
#     path='/',
#     status_code=status.HTTP_200_OK,
#     summary="Home's app and Hello World",
#     tags=['home'])
# def home_page(request: Request):
#     '''
#     Home's app & Hello World FastAPI

#     This path operation say hellow to everybody user in the app

#     Parameters: Nothing

#     Returns   : A json with the greeting information
#     '''
#     return template.TemplateResponse('home_page.html', {"request": request})

# ROUTERS:
app.include_router(user_router)
app.include_router(thought_router)
app.include_router(question_router)
app.include_router(answer_router)
