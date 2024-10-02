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

# Definir el componente para el botón de WhatsApp en desktop
def whatsapp_button_desktop():
    return rx.card(
        rx.text(cta_texto),  # Incluir texto solo en desktop
        simpleicons("whatsapp", brand_color=True),
        align_items="flex-start",
        z_index="200",
        position="fixed",
        bottom="50px",
        right="50px",
        max_width=Size.CARDSIZE.value,
        background_color=rx.color_mode_cond(
            light=rx.color("grass", 4),  # Color para tema claro
            dark=rx.color("grass", 7)    # Color para tema oscuro
        ),
        on_click=lambda: rx.redirect(whatsapp_link, external=True),  # Redirige al enlace de WhatsApp
        border_radius="1em",
        
        # Sombra verde
        box_shadow="rgba(38, 222, 129, 0.8) 0 15px 30px -10px",
        
        # Fondo azul con verde (sin violeta)
        background_image=rx.color_mode_cond(
            light="linear-gradient(144deg, #0080FF, #00AF80 50%, #00FF80)",  # Degradado azul a verde para tema claro
            dark="linear-gradient(144deg, #0040FF, #008080 50%, #00FF80)"    # Degradado azul a verde para tema oscuro
        ),
        
        box_sizing="border-box",
        color=rx.color_mode_cond(
            light="black",  # Texto negro en tema claro
            dark="white"    # Texto blanco en tema oscuro
        ),
        opacity=1,
        
        # Efecto hover
        _hover={
            "opacity": 0.5,  # Opacidad al hacer hover
        },
    )

# Definir el componente para el botón de WhatsApp en mobile/tablet (sin texto)
def whatsapp_button_mobile():
    return rx.card(
        simpleicons("whatsapp", brand_color=True),
        align_items="flex-start",
        z_index="200",
        position="fixed",
        bottom="80px",
        right="30px",
        max_width=Size.SUPERBIG.value,
        background_color=rx.color_mode_cond(
            light=rx.color("grass", 4),  # Color para tema claro
            dark=rx.color("grass", 7)    # Color para tema oscuro
        ),
        on_click=lambda: rx.redirect(whatsapp_link, external=True),  # Redirige al enlace de WhatsApp
        border_radius="1em",
        
        # Sombra verde
        box_shadow="rgba(38, 222, 129, 0.8) 0 15px 30px -10px",
        
        # Fondo azul con verde (sin violeta)
        background_image=rx.color_mode_cond(
            light="linear-gradient(144deg, #0080FF, #00FF80 50%, #00FF80)",  # Degradado azul a verde para tema claro
            dark="linear-gradient(144deg, #0040FF, #008080 50%, #00FF80)"    # Degradado azul a verde para tema oscuro
        ),
        
        box_sizing="border-box",
        color=rx.color_mode_cond(
            light="black",  # Texto negro en tema claro
            dark="white"    # Texto blanco en tema oscuro
        ),
        opacity=1,
        
        # Efecto hover
        _hover={
            "opacity": 0.5,  # Opacidad al hacer hover
        },
    )

# Componente que maneja las dos versiones según el dispositivo
def whatsapp_button():
    return whatsapp_button_mobile()  # Solo mostrar en mobile/tablet
        