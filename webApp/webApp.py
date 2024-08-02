"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
import reflex as rx
from .components.components import navbar_user, image_component,footer 
from .styles.styles import color , accent_color

def index():
    """The main view."""
    return  rx.vstack(
            navbar_user(), 
            rx.spacer(),             
            image_component(),
            rx.spacer(),  
            footer(),
            justify="end",
            spacing="6",     
            bg=rx.color(color, 2),
            width="100%",
            height="100%"
            ),
          

app = rx.App(theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color=accent_color,
        
    )
   )
app.add_page(index)

