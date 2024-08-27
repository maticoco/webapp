from sqlmodel import create_engine



def connect():
    #engine=create_engine("dialect[+driver]://user:password@host/dbname")
    engine=create_engine(f"sqlite:///reflex.db")
    return engine