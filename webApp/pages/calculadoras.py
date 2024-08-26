import reflex as rx
from ..components.components import navbar_user,footer, color , cards_grid
from ..repository.login_state import require_login, LoginState
from ..styles.styles import Size

CATALOG_ROUTE = "/calcs"


@rx.page(route=CATALOG_ROUTE,title="Calculadoras")

#@require_login
def calcs_page() -> rx.Component:
    return rx.vstack(            
            navbar_user(),
            rx.flex(           
            cards_grid(),
            padding=Size.DEFAULT.value
            ),
            footer(),
            
            bg=rx.color(color, 2),
            ) 


