import reflex as rx
from .repository.base_state import State
from .repository.login_state import require_login, LoginState
from .routes import LOGIN_ROUTE
from .components.components import login_component






@rx.page(route=LOGIN_ROUTE)
def login_page() -> rx.Component:
    """Render the login page.

    Returns:
        A reflex component.
    """
   

    return login_component()


def logo()-> rx.Component:
    return  rx.image(src='/logo_cerrajeria.png',width="300px", border_radius="15px 50px")
            

