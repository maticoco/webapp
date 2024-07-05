import  reflex as rx
import requests as rq
import re
from reflex.style import toggle_color_mode
from .components.components import navbar_user,footer, about_component, color 

@rx.page(route="/about", title="Sobre Nosotros")
def about() -> rx.Component:
    return rx.box(            
            navbar_user(),                                  
            about_component(),                       
            footer(),        
                        
            bg=rx.color(color, 2), 
            )


