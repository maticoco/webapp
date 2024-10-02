import reflex as rx
from ..styles.styles import Size, color
from ..service.email_service import EmailServiceState  # Importar el estado del servicio de correo
from ..components.notify import notify_component  # Importar el componente de notificación


def form_field(label: str, placeholder: str, type: str, name: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(placeholder=placeholder, type=type,required=True),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )


def contact_form() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.card(
                rx.flex(
                    rx.hstack(
                        rx.badge(
                            rx.icon(tag="mail-plus", size=32),
                            color_scheme=color,
                            radius="full",
                            padding="0.65rem",
                        ),
                        rx.vstack(
                            rx.heading(
                                "Envianos un mensaje",
                                size="4",
                                weight="bold",
                            ),
                            rx.text(
                                "Completa el formulario para que nos contactemos",
                                size="2",
                            ),
                            spacing="1",
                            height="100%",
                        ),
                        height="100%",
                        spacing="4",
                        align_items="center",
                        width="100%",
                    ),
                    rx.form.root(
                        rx.flex(
                            rx.flex(
                                form_field("Nombre", "Nombre", "text", "first_name"),
                                form_field("Apellido", "Apellido", "text", "last_name"),
                                spacing="3",
                                flex_direction=["column", "row", "row"],
                                width="100%",
                            ),
                            rx.flex(
                                form_field("Email", "user@reflex.dev", "email", "email"),
                                form_field("Telefono", "Telefono", "tel", "phone"),
                                spacing="3",
                                flex_direction=["column", "row", "row"],
                                width="100%",
                            ),
                            rx.flex(
                                rx.text(
                                    "Mensaje",
                                    style={"font-size": "15px", "font-weight": "500"},
                                ),
                                rx.text_area(
                                    placeholder="Escribe tu mensaje aquí...",
                                    name="message",
                                    resize="vertical",
                                    auto_height=True,
                                    min_height="150px",
                                    required=True
                                ),
                                direction="column",
                                spacing="1",
                                width="100%",
                            ),
                            rx.form.submit(
                                rx.button("Enviar"),
                                as_child=True,
                            ),
                            direction="column",
                            spacing="2",
                            width="100%",
                        ),
                        on_submit=EmailServiceState.handle_submit,
                        reset_on_submit=True,
                    ),
                    max_width=["90%", Size.FORMCONTACT.value],
                    direction="column",
                    spacing="4",
                    width="100%",
                    height="auto",
                    align="start",
                ),
                size="3",
                max_width=["100%", "60em"],
                height="auto",
            ),
            justify="center",
            align="center",
            width="100%",
            height="100%",
            padding_bottom="5rem",
        ),
        # Mostrar la notificación cuando el estado lo permita
        rx.cond(EmailServiceState.notification == "",rx.text(""),
            rx.cond(EmailServiceState.notification == "Correo enviado con éxito",
                notify_component(
                    EmailServiceState.notification,
                    "circle_check_big" ,
                    "green" 
                ),rx.cond(EmailServiceState.notification == "Enviando...",
                    notify_component(
                        EmailServiceState.notification,
                        "circle_alert" ,
                        "blue" 
                        ),
                    notify_component(
                        EmailServiceState.notification,
                        "circle_alert" ,
                        "red" 
                        )                
                        )   
                    )
                ),
        
        width="100vw",
        height="60vh",
        justify="center",
        align="center",
        padding="2rem",
        margin_top="20vh",
        margin_bottom="20vh",
        spacing="2",
    )
