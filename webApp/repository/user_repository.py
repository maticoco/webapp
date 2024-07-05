from ..model.user import User
from ..model.auth_session import AuthSession
from .connect_db import connect
from sqlmodel import Session, select



def select_all():
    engine=connect()
    with Session(engine) as session:
        query = select(User)
        return session.exec(query).all()
    

def select_user_by_username(username: str):
    engine = connect()
    with Session(engine) as session:
        query = select(User).where(User.username == username)
        return session.exec(query).all()
    
def select_user_by_id(id: int):
    engine = connect()
    with Session(engine) as session:
        query = select(User).where(User.id == id)
        return session.exec(query).all()

def create_user(user: User ):
    engine = connect()
    with Session(engine) as session:
        session.add(user)
        session.commit()
        query = select(User)
        return session.exec(query).all()
    
def delete_user(username: str):
    engine = connect()
    with Session(engine) as session:
        query=select(User).where(User.username == username)
        user_delete= session.exec(query).one()
        session.delete(user_delete)
        session.commit()
        query = select(User)
        return session.exec(query).all()
    
def select_all_exp():
    engine = connect()
    with Session(engine) as session:
        query = select(User).join(AuthSession,AuthSession.user_id == User.id,isouter=True)
        return session.exec(query).all()