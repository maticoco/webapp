import  reflex as rx
from reflex.style import toggle_color_mode
from ..components.components import navbar_user,footer, about_component, color
from ..components.contact_form import contact_form

@rx.page(route="/contact", title="Contacto")
def contact() -> rx.Component:
    return rx.box(            
            navbar_user(),                                  
            contact_form(),                       
            footer(),        
                        
            bg=rx.color(color, 2), 
            )
