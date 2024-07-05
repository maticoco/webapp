import reflex as rx
from .components.components import navbar_user,footer, color , cards_grid
from .repository.login_state import require_login, LoginState

CATALOG_ROUTE = "/calcs"


@rx.page(route=CATALOG_ROUTE,title="Calculadoras")

def calcs_page() -> rx.Component:
    return rx.box(            
            navbar_user(),
                       
            cards_grid(),
              
            footer(),
            rx.flex(
                top="0px",
                width="100%",
                ),
            bg=rx.color(color, 2),
            ) 


