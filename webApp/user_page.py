import  reflex as rx

from .model.auth_session import AuthSession
from .service.user_service import select_all_user_service, select_user_by_username_service,create_user_service,delete_user_service,select_all_exp_service 
from .notify import notify_component
import asyncio
from .components.components import create_user_dialogo_componenet, search_user_component,table_user
from .repository.users_state import UserState

@rx.page(route='/users', title="user", on_load=UserState.get_all_user)
def user_page() -> rx.Component:
    return  rx.flex(
        rx.heading('Usuarios', align='center'),
        rx.hstack(
            search_user_component(),
            create_user_dialogo_componenet(),
            justify='center',
            style={'margin-top': '30px'}
        ),
        table_user(UserState.users),
        rx.cond(
            UserState.error != '',
            notify_component(UserState.error, 'shield-alert','yellow')
        ),
        direction='column',
        style={'width': '60vw','margin': 'auto'}
    )
