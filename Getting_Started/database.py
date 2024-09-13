from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# fist define a databse connection parameters


DB_URL = "mysql+pymysql://{db_username}:{db_password}@localhost:3306/{db_name}"
engine = create_engine(DB_URL, echo=True)

# define a session 

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

# create a base that can be used to store the schemas within the database
Base = declarative_base()