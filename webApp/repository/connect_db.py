from sqlmodel import create_engine
from db_googlecloud import USER, USERPASSWORD, DB_NAME, REGION, INSTANCE_NAME

def connect():
    #engine=create_engine("dialect[+driver]://user:password@host/dbname")
    engine=create_engine(f"mysql+pymysql://{USER}:{USERPASSWORD}@localhost:3306/{DB_NAME}")
    return engine