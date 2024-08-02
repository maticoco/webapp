# import reflex as rx
# from db_googlecloud import USER,USERPASSWORD

# config = rx.Config(
#     app_name="webApp",
#     db_url= f"mysql+pymysql://{USER}:{USERPASSWORD}@34.95.173.232:3306/lithe-record-429615-b8:southamerica-east1:ljr-app",
#     #db_url="mysql+pymysql://root:mati@localhost:3306/webapp",
# )


import reflex as rx



from db_googlecloud import USER, USERPASSWORD, DB_NAME, REGION, INSTANCE_NAME

from google.cloud.sql.connector import Connector, IPTypes
import pymysql
import sqlalchemy
import google.auth

credentials, project_id = google.auth.default()


# initialize parameters
INSTANCE_CONNECTION_NAME = f"{project_id}:{REGION}:{INSTANCE_NAME}" # i.e demo-project:us-central1:demo-instance




config = rx.Config(
    app_name="webApp",
    #db_url= getconn(),
    db_url=f"mysql+pymysql://{USER}:{USERPASSWORD}@localhost:3306/{DB_NAME}",
    
    #funciono en local
    #db_url="mysql+pymysql://root:mati@localhost:3306/webapp",
)

