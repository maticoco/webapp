from ..repository.user_repository import select_all,create_user, select_all_exp, delete_user, select_user_by_username, select_user_by_id
from ..model.user import User

def select_all_user_service():
    users = select_all()
    print(users)
    return users


    
def select_user_by_username_service(username: str):
    if(len(username) != 0):
        return select_user_by_username(username)
    else:
        return select_all_user_service()
        
    
def select_user_by_idusers_service(idusers: int):
    if idusers != 0:
        return select_user_by_id(idusers)
     

    
def create_user_service(username: str , password: str, enabled: bool):
    user = select_user_by_username(username)
    if(len(user) == 0):
        user_save = User(username= username, password= password, enabled=enabled)
        return create_user(user_save)
    else:
        print('El usuario ya existe')
        raise BaseException('El usuario ya existe')
    
def delete_user_service(username: str):
    return delete_user(username=username)

def select_all_exp_service():
    users=select_all_exp()
    print(users)
    return users
