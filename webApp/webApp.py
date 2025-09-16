"""Welcome to Reflex! This file outlines the steps to create a basic app."""


import reflex as rx
from .components.components import navbar_user, image_component,footer
from .components.whatsapp_button2 import whatsapp_button_mobile 
from .styles.styles import color , accent_color,style

def index():
    """The main view."""
    return  rx.vstack(
            navbar_user(),           
            image_component(),
            whatsapp_button_mobile(),
            footer(),    
            bg=rx.color(color, 2),
            width="100%",
            height="100vh"
            ),
          

app = rx.App(theme=style)
app.add_page(index)


