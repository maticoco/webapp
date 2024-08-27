"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .components.components import navbar_user, image_component,footer 
from .styles.styles import color , accent_color,style

def index():
    """The main view."""
    return  rx.vstack(
            navbar_user(), 
            rx.spacer(height="100%"),             
            image_component(),
            rx.spacer(height="100%"),  
            footer(),
            
            spacing="9",     
            bg=rx.color(color, 2),
            width="100%",
            
            ),
          

app = rx.App(theme=style)
app.add_page(index)


