import reflex as rx
from enum import Enum

color = "orange"
accent_color = "amber"


style=theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color=accent_color,
        scaling="100%"
        
        
    )

class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    TITLE = "1.5em"
    BIG = "2em"
    SUPERBIG = "5em"
    CARDSIZE = "7em"
    CALLOUTSIZE = "9em"
    IMGBIG = "15em"
    FORMCONTACT = "38em"
    FORMCONTACTBIG = "88em"
    SLIDERDESKTOP = "720px"  # Tamaño para desktop
    SLIDERMOBILE = "300px"   # Tamaño más pequeño para mobile/tablet


button_title_style = dict(
    font_size = Size.TITLE.value
)

button_body_style = dict(
    font_size = Size.DEFAULT.value
)


# Definir fuentes
font_families = {
    "body": "Roboto",       # Fuente para el texto general
    "heading": "Poppins",   # Fuente para los encabezados
}

# Estilos generales
global_styles = {
    "font_family": font_families["body"],
    "font_size": "16px",
}

# Estilos para las notificaciones
style_notify_dark = {
    'position': 'fixed',
    'top': Size.CALLOUTSIZE.value,
    'right': '20px',
    'z-index': '10000',
    'background-color': '#333',
    'padding': '20px 30px',
    'border-radius': '8px',
    'border': '2px solid #555',
    'box-shadow': '0 8px 16px rgba(0, 0, 0, 0.6)',
    'font-family': font_families["body"],
    'font-size': Size.DEFAULT.value,
    'color': '#fff',
}


# Estilos para componentes específicos
component_styles = {
    # Estilos para el texto
    rx.text: {

        "font_size": "1rem",
        "line_height": "1.5",
    },
    # Estilos para los botones
    rx.button: {
        "padding": "0.75em 1.25em",
        "font_size": "1rem",


        "border": "none",
        "border_radius": "0.25rem",
        "cursor": "pointer",

    },
    # Estilos para los contenedores
    rx.box: {
        "padding": "1em",
        "margin": "1em 0",

        "border_radius": "0.25rem",
        "box_shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
    },
    # Estilos para las tarjetas
    rx.card: {
        "padding": "1.5em",
        "margin": "1em",

        "border_radius": "0.5rem",
        "box_shadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
    },
    # Estilos para los encabezados
    rx.heading: {
        "font_size": "2rem",
        "font_weight": "600",
        "margin_bottom": "0.5em",
    },
    # Estilos para los enlaces
    rx.link: {

        "text_decoration": "none",
        "_hover": {
            "text_decoration": "none",   
        },
    },
}
style_notify = {
    'position': 'fixed',
    'top': '0px',
    'right': '0px',
    'margin': '10px 10px'
}