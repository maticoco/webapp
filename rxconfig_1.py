# import reflex as rx
# from db_googlecloud import USER,USERPASSWORD

# config = rx.Config(
#     app_name="webApp",
#     db_url= f"mysql+pymysql://{USER}:{USERPASSWORD}@34.95.173.232:3306/lithe-record-429615-b8:southamerica-east1:ljr-app",
#     #db_url="mysql+pymysql://root:mati@localhost:3306/webapp",
# )


import reflex as rx



from google.cloud.sql.connector import Connector, IPTypes
import pymysql
import sqlalchemy
import google.auth
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

credentials, project_id = google.auth.default()


# initialize parameters
INSTANCE_CONNECTION_NAME = f"{project_id}:{db_region}:{db_instance}" # i.e demo-project:us-central1:demo-instance




config = rx.Config(
    app_name="webApp",
    #db_url= getconn(),
    db_url=f"mysql+pymysql://{db_user}:{db_password}@{db_host}:3306/{db_name}",
    
    #funciono en local
    #db_url="mysql+pymysql://root:mati@localhost:3306/webapp",
)

