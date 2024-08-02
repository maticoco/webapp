from sqlmodel import create_engine

def connect():
    #engine=create_engine("dialect[+driver]://user:password@host/dbname")
    engine=create_engine("mysql+pymysql://root:mati@localhost:3306/webapp")
    return engine