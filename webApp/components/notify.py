import reflex as rx
from ..styles.styles import style_notify_dark 

# Componente para mostrar notificaciones
def notify_component(message: str, icon_notify: str, color: str) -> rx.Component:
    
    return rx.callout(
        message,
        icon=icon_notify,
        style=style_notify_dark,
        color_scheme=color
    )
