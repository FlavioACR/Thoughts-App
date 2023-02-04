# DEPENDENCYS:
# Python
from typing import Optional, List
from datetime import date
# Pydantic
from pydantic import BaseModel, Field
# FastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from fastapi import status

#from middlewares.error_handler import ErrorHandler
#from routers.users import movie_router
#from routers.users import user_router

# Routers:
from routers.users import user_router
from routers.thoughts import thought_router

app = FastAPI()
app.title = "My Thoughts APP with FastAPI"
app.version = "0.0.1"

#app.add_middleware(ErrorHandler)


Base.metadata.create_all(bind=engine)

@app.get(
    path='/',
    status_code=status.HTTP_200_OK,
    summary="Home's app and Hello World",
    tags=['home'])
def home_and_helloworld():
    '''
    Home's app & Hello World FastAPI 

    This path operation say hellow to everybody user in the app

    Parameters: Nothing
    
    Returns   : A json with the greeting information
    '''
    return HTMLResponse('<h1>HELLO WORD AND WELCOME TO THE APP THOUGHTS APP</h1>')

# ROUTERS:
app.include_router(user_router)
app.include_router(thought_router)