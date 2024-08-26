from sqlmodel import create_engine
from dotenv import load_dotenv

import os

load_dotenv()

# Ahora puedes acceder a las variables de entorno
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_instance= os.getenv('DB_INSTANCE')
db_region = os.getenv('DB_REGION')
project_id = os.getenv('DB_PROJECTID')

# initialize parameters
INSTANCE_CONNECTION_NAME = f"{project_id}:{db_region}:{db_instance}" # i.e demo-project:us-central1:demo-instance


def connect():
    #engine=create_engine("dialect[+driver]://user:password@host/dbname")
    engine=create_engine(f"mysql+pymysql://{db_user}:{db_password}@localhost:3306/{db_name}")
    return engine