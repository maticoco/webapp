import  reflex as rx
from .model.user import User
from .model.auth_session import AuthSession
from .service.user_service import select_all_user_service, select_user_by_username_service,create_user_service,delete_user_service,select_all_exp_service 
from .notify import notify_component
import asyncio
from .registration import registration_page

class UserState(rx.State):
    pass
    users: list[User]
    user_search: str
    error: str = ''

    @rx.background
    async def get_all_user(self):
        async with self:
            self.users = select_all_user_service()
 
    @rx.background
    async def get_user_by_username(self):
        async with self:
            self.users = select_user_by_username_service(self.user_search)

    

    async def handleNotify(self):
        async with self:
            await asyncio.sleep(2)
            self.error = ''

    @rx.background
    async def create_user(self, data: dict):
        async with self:
            try:
                self.user = create_user_service(username=data['username'], password=data['password'], isactive=1, ip='')
                
            except BaseException as be:
                print(be.args)
                self.error = be.args
        await self.handleNotify()

    @rx.background
    async def delete_user(self, email):
        async with self:
            self.users = delete_user_service(email)

    def search_on_change(self, value: str):
        self.user_search = value


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


def table_user(list_user: list[User])-> rx.Component:
    return rx.table.root(
       rx.table.header(
           rx.table.row(
               rx.table.column_header_cell('UserID'),
               rx.table.column_header_cell('Username'),               
               rx.table.column_header_cell('Whitelist'),

               
           )
       ),
       rx.table.body(
            rx.foreach(list_user, row_table)
       ) 
    )

def row_table(user: User)-> rx.Component:
    return rx.table.row(
        rx.table.cell(user.id),
        rx.table.cell(user.username),
        rx.table.cell(user.enabled),

        
        rx.table.cell(rx.hstack(            
            delete_user_dialogo_component(user.username)
        ))
    )

def search_user_component() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder='Ingrese usuario', on_change=UserState.search_on_change),
        rx.button ('Buscar Usuario' , on_click= UserState.get_user_by_username)
    )


def create_user_form()-> rx.Component:
    return rx.form(
                rx.vstack(
                    rx.input(
                        placeholder='Nombre de usuario',
                        name= 'username'
                    ),
                    rx.input(
                        placeholder='Email',
                        name= 'Email'
                    ),
                    rx.input(
                        placeholder='Contraseña',
                        name= 'password',
                        type='password'
                    ),
                    
                    rx.dialog.close(
                        rx.button('Guardar', type='submit')
                    ),
                ),
                on_submit=UserState.create_user,
    )

def create_user_dialogo_componenet() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button('Crear Usuario') ),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title('Crear Usuario'),
                #create_user_form(),
                registration_page(),
                justify='center',
                align='center',
                direction='column',
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button('Cancelar', color_scheme='gray', variant= 'soft')
                ),
                spacing='3',
                margin_top='16px',
                justify='end',
            ),
            style={'width': '300px'}
        ),
    )

def delete_user_dialogo_component(username: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon('trash-2'))),
        rx.dialog.content(
            rx.dialog.title('Eliminar usuario'),
            rx.dialog.description('Esta seguro de querer eliminar el usuario '+ username),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        'Cancelar',
                        color_scheme='gray',
                        variant='soft'
                    ),
                ),
                rx.dialog.close(
                    rx.button('Confirmar', on_click=UserState.delete_user(username)),    
                ),

                spacing='3',
                margin_top='16px',
                justify='end',
            )
        )
    )