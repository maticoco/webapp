import reflex as rx
from ..components.components import singup_component
from ..styles.styles import Size
from ..repository.registration import RegistrationState

from ..routes import REGISTER_ROUTE

@rx.page(route=REGISTER_ROUTE)
def registration_page() -> rx.Component:
    """Render the registration page.

    Returns:
        A reflex component.
    """
    

    return rx.box(singup_component(),
        padding= "10em",
        )
        
        # position="absolute",
        # top="50vh",
        # left="50vh"

        # position="absolute",
        # size="auto",
        # top="30vh",
        # left="90vh",

     
            
