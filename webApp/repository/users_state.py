import  reflex as rx
from ..service.user_service import select_all_user_service, select_user_by_username_service,create_user_service,delete_user_service,select_all_exp_service 
from ..notify import notify_component
import asyncio
from ..model.user import User

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

