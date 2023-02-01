# File to configurate de database using a ORM SQLAlchemy for python.

# Dependecys:
# Python:
import os
# sqlalchemy:
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base # This help to work with the database's tables.

# We save the name of the database as string in a variable:
sqlite_file_name = "../database.sqlite"

# Read the actual directory of this file:
base_dir = os.path.dirname(os.path.realpath(__file__))

# We create the url´s database.
#   Joining the current path + the name of the data base:
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# Create the engine that represent the engine of the database, for this
# we use the function, create_engine(), this function recieve the url y el parametro echo="True":
engine = create_engine(database_url, echo=True)

# Create a session in the data base, linked with the engine bata base:
Session = sessionmaker(bind=engine)

Base = declarative_base()