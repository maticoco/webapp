import os
import reflex as rx
from reflex_simpleicons import simpleicons
from ..styles.styles import color, accent_color, Size
from dotenv import load_dotenv
load_dotenv(override=True)
# Obtener el número de WhatsApp de la variable de entorno
whatsapp_number = os.getenv("WHATSAPP_NUMBER")  # Valor por defecto si no está definido

whatsapp_message = "¡Hola! Estoy contactandome desde la pagina web."
cta_texto = "Chatea con nosotros" 
# Definir el enlace de WhatsApp con el mensaje
whatsapp_link = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"

def whatsapp_icon():
    return rx.image(
        src="/whatsapp.svg",  # Ruta de la imagen
        width="50px",          # Ajusta el ancho de la imagen
        height="50px",         # Ajusta la altura de la imagen
        border_radius="50%",   # Hace que la imagen sea circular (opcional)
        
    )


def whatsapp_button_mobile():
    return rx.card(
        whatsapp_icon(),  # Ícono de WhatsApp
        position="fixed",
        bottom=Size.SUPERBIG.value,
        right=Size.BIG.value,
        z_index="1000",
        background_color="#25D366",
        border_radius="50%",
        padding="15px",
        box_shadow="0px 4px 10px rgba(0, 0, 0, 0.3)",  # Sombra para darle profundidad
        _hover={
            "opacity": "0.8",
            "box_shadow": "0px 4px 15px rgba(0, 0, 0, 0.4)",
        },
        on_click=lambda: rx.redirect(whatsapp_link, external=True),
    )