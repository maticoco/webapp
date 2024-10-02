import reflex as rx
from reflex.style import toggle_color_mode
from ..components.components import navbar_user, footer, about_component, color
from ..components.whatsapp_button import whatsapp_button  

@rx.page(route="/about", title="Sobre Nosotros")
def about() -> rx.Component:
    return rx.flex(            
        navbar_user(),                                  
        about_component(),
        whatsapp_button(),                        
        footer(),        
        direction="column",
        #justify="center",  # Para que el contenido ocupe el espacio y el footer esté al final
        height="100vh",  # Asegura que el contenedor ocupe toda la pantalla
        bg=rx.color(color, 2),
        width="100%", 
    )
