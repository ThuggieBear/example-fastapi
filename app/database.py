from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import psycopg2
from psycopg2.extras import RealDictCursor
from . config import settings

# 'postgresql://<username>:<password>@<ip_address/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

#sqlalchemy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


''' sql directly
while True:  
    # attempt to connect to database
    # RealDictCursor returns column names
    try:
        # connection to database
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres',  
        password = 'Mooseyfate24', cursor_factory = RealDictCursor)
        # database interface
        cursor = conn.cursor()
        print("Database connection was successful")
        break # break out of while loop
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)  # retry connection every 2 seconds
        '''