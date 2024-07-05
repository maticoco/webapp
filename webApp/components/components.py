import reflex as rx
from reflex.style import toggle_color_mode

from ..repository.base_state import State
from ..repository.registration import RegistrationState
from ..repository.upload_state import UploadState
from ..repository.login_state import require_login, LoginState
from ..routes import GOLMM_ROUTE, LOGIN_ROUTE , REGISTER_ROUTE

from ..styles.styles import color , accent_color, Spacer


def dark_light_theme()-> rx.Component: 
    return  rx.button(
                rx.color_mode_cond(
                        light=rx.icon("moon"),
                        dark=rx.icon("sun"),
                        ),
                color=rx.color_mode_cond(light=rx.color(color, 7), dark=rx.color(color, 1)),
                background_color=rx.color_mode_cond(
                        light=rx.color(color, 4), dark=rx.color(color, 7)
                        ),
                on_click=toggle_color_mode,
                     )
                
def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar_user() -> rx.Component:
    return      rx.box(
                rx.hstack(dark_light_theme(),justify="end",padding="1em"),
                rx.desktop_only(
                    rx.hstack(
                        rx.hstack(
                            rx.image(
                                src="/logo_cerrajeria.png",
                                width=Spacer.SUPERBIG.value,
                                height="auto",
                                border_radius="25%",
                                ),
                            rx.heading(
                                "Cerrajeria Automotriz", size="7", weight="bold",color_scheme=color
                                ),
                            align_items="center",
                            padding="1em"
                            ),
                        rx.hstack(
                            navbar_link("Home", "/#"),
                            navbar_link("Sobre Nosotros", "/about"),
                            navbar_link("Calculadoras", "/calcs"),
                            navbar_link("Contacto", "/#"),
                            spacing="5",
                            ),
                            username(),                                   
                            user_menu(),
                            login_menu_desktop(),                     
                            justify="between",
                            align="center",
                            padding_x="1em",
                            padding_bottom="0.5em"
                            
                                ),
                            ),
                rx.mobile_and_tablet(
                    rx.hstack(
                        rx.hstack(
                            rx.image(
                                src="/logo_cerrajeria.png",
                                width=Spacer.BIG.value,
                                height="auto",
                                border_radius="25%",
                            ),
                            rx.heading(
                                "Cerrajeria Automotriz", size="6", weight="bold",color_scheme=color
                            ),
                            align_items="center",
                        ),
                        username(),
                        user_menu(),
                        login_menu_movile(),
                                ),
                        justify="between",
                        align_items="center",
                    ),
                
                top = "0",
                bg=rx.color(color, 3),
                position= "sticky",
                width="100%",
                z_index="200",
            )
    
def username()-> rx.Component:
    return rx.heading(
                    State.authenticated_user.username, size="7", weight="bold",color_scheme=color
                    )

def image_component()-> rx.Component:
    return rx.flex(
            rx.image(src='/background.jpg')
            ,
            width="100%",
            direction="column",
            align="center",
            justify="center",
            
        )

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)

def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "PRODUCTS", size="4", weight="bold", as_="h3"
        ),
        footer_item("Web Design", "/#"),
        footer_item("Web Development", "/#"),
        footer_item("E-commerce", "/#"),
        footer_item("Content Management", "/#"),
        footer_item("Mobile Apps", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            "RESOURCES", size="4", weight="bold", as_="h3"
        ),
        footer_item("Blog", "/#"),
        footer_item("Case Studies", "/#"),
        footer_item("Whitepapers", "/#"),
        footer_item("Webinars", "/#"),
        footer_item("E-books", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href,is_external=True)

def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", href="https://www.instagram.com/cerrajeria_ljr/"),
        social_link("map", href="https://maps.app.goo.gl/esMx5Xa4nutvsn37A"),

        spacing="3",
        justify="end",
        width="100%",
    )

def footer() -> rx.Component:
    return      rx.el.footer(
                rx.vstack(
                    rx.divider(),
                    rx.hstack(
                        rx.hstack(
                            footer_item("Privacy Policy", "/#"),
                            footer_item("Terms of Service", "/#"),
                            spacing="4",
                            align="center",
                            width="100%",
                        ),
                        socials(),
                        justify="between",
                        width="100%",
                    ),
                    spacing="5",
                    width="100%",
                ),
                
                width="100%",
                padding="1em",
                bg=rx.color(color, 3),
                )

def login_default() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/logo.jpg",
                    width="2.5em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading(
                    "Sign in to your account",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Username",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="username",
                    type="username",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                    ),
                    rx.link(
                        "Forgot password?",
                        href="#",
                        size="3",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    placeholder="Enter your password",
                    type="password",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Sign in", size="3", width="100%"),
            rx.center(
                rx.text("New here?", size="3"),
                rx.link("Sign up", href="#", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="28em",
        width="100%",
    )

def user_menu() -> rx.Component:
    return  rx.menu.root(
                rx.menu.trigger(
                    rx.icon_button(
                        rx.icon("user"),
                        size="2",
                        radius="full",
                    )
                ),
                rx.menu.content(
                    rx.menu.item("Settings"),
                    rx.menu.item("Earnings"),
                    rx.menu.separator(),
                    rx.menu.item("Log out",on_click=State.do_logout),
                    bg=rx.color(color, 2),
                ),
                justify="end",
            ),
          
def login_menu_movile() -> rx.Component:
    return  rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Log in",on_click=rx.redirect(LOGIN_ROUTE)),
                        rx.menu.item("Sign up",on_click=rx.redirect(REGISTER_ROUTE)),
                    ),
                    justify="end",
                )

def login_menu_desktop() -> rx.Component:
    return  rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                        on_click=rx.redirect(REGISTER_ROUTE)
                    ),
                    
                    rx.button("Log In", size="3",on_click=rx.redirect(LOGIN_ROUTE)),
                    spacing="4",
                    justify="end"
                ),

def cards_grid()->rx.Component:
    return rx.grid(
                rx.card(
                        rx.inset(
                            rx.image(
                                src="/5U0920830K.webp",
                                padding="0.5em",
                                size="4",
                                border_radius="15px 50px",
                                border="5px solid #555",
                            ),
                            side="top",
                            pb="current",
                        ),
                        rx.text(
                            "Gol G6 ",rx.text.strong(("Magnetti Marelli Nec + 95320"),as_="label",
                        ),
                        
                    ),
                    rx.button("Load Dump", size="3",on_click=rx.redirect(GOLMM_ROUTE)),
                    width="20em",
                    height="20em"
                ),
                gap="1rem",
                
                width= "100%",
                height="43em",
                padding_x="20em",
                padding_y="2em"
                
            )

def signup_default_icons() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                        src="/logo_cerrajeria.png",
                        width="5.25em",
                        height="auto",
                        border_radius="25%",
                        
                ),
                rx.heading(
                    "Creacion de cuenta",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.form(
            rx.vstack(
                rx.text(
                    "Nombre de Usuario",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("user")),
                    placeholder="nombre_usuario",
                    id="username",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Contraseña",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    placeholder="Ingrese su Contraseña",
                    type="password",
                    id="password",
                    size="3",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("key")),#slot(rx.icon("lock")),
                    
                    placeholder="Reingrese su Contraseña",
                    type="password",
                    id="confirm_password",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            
            rx.button("Sign in", type="submit" ,size="3", width="100%"),
            on_submit=RegistrationState.handle_registration
            ),
            

            rx.center(
                rx.text("Ya estas registrado?", size="3"),
                rx.link("Log in", href="/login", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
                width="100%",
            ),
            spacing="6",
            width="100%",
        ),
        max_width="28em",
        size="4",
        width="100%",
    )

def singup_component() -> rx.Component:
    register_form = signup_default_icons()
    return rx.fragment(
        rx.cond(
            RegistrationState.success,
            rx.chakra.vstack(
                rx.chakra.text("Registration successful!"),
                rx.chakra.spinner(),
            ),
            rx.chakra.vstack(
                rx.cond(  # conditionally show error messages
                    RegistrationState.error_message != "",
                    rx.chakra.text(RegistrationState.error_message),
                ),
                register_form,
                padding_top=Spacer.SMALL,
            ),
        ),
        
    )

def about_component()-> rx.Component:
    return rx.scroll_area(
                rx.flex(
                    rx.text(
                        """Three fundamental aspects of typography are legibility, readability, and
                    aesthetics. Although in a non-technical sense “legible” and “readable”
                    are often used synonymously, typographically they are separate but
                    related concepts.""",
                    ),
                    rx.text(
                        """Legibility describes how easily individual characters can be
                    distinguished from one another. It is described by Walter Tracy as “the
                    quality of being decipherable and recognisable”. For instance, if a “b”
                    and an “h”, or a “3” and an “8”, are difficult to distinguish at small
                    sizes, this is a problem of legibility.""",
                    ),
                    rx.text(
                        """Typographers are concerned with legibility insofar as it is their job to
                    select the correct font to use. Brush Script is an example of a font
                    containing many characters that might be difficult to distinguish. The
                    selection of cases influences the legibility of typography because using
                    only uppercase letters (all-caps) reduces legibility.""",
                    ),
                    direction="column",
                    spacing="4",
                    padding="10em"
                    
                ),
                type="always",
                scrollbars="vertical",
                style={"height": 720},
                
            )

def upload() -> rx.Component:
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button("Select File", color=color, bg="white", border=f"1px solid {color}"),
                rx.text("Drag and drop files here or click to select files"),
            ),
            id="upload2",
            multiple=False,
            max_files=1,
            disabled=False,
            no_keyboard=True,
            on_drop=UploadState.handle_upload(rx.upload_files(upload_id="upload2")),
            border=f"1px dotted {color}",
            padding="5em",
        ),
        padding="5em",
    )

def result_card() -> rx.Component:
    return rx.card(
        rx.text(UploadState.decoded_data,white_space="pre"),
        
        size="5",
        border=f"1px solid {color}",
        width="100%",
        height="100%"
    )

def login_default_icons() -> rx.Component:
    return rx.card(
                rx.vstack(
                    rx.center(
                        rx.image(
                            src="/logo_cerrajeria.png",
                            width="5.5em",
                            height="auto",
                            border_radius="25%",
                        ),
                        rx.heading(
                            "Sign in to your account",
                            size="6",
                            as_="h2",
                            text_align="center",
                            width="100%",
                        ),
                        direction="column",
                        spacing="5",
                        width="100%",
                    ),
                    rx.form(
                    rx.vstack(
                        rx.text(
                            "Username",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            placeholder="Nombre de usuario",
                            id="username",
                            size="3",
                            width="100%",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                "Password",
                                size="3",
                                weight="medium",
                            ),
                            rx.link(
                                "Forgot password?",
                                href="#",
                                size="3",
                            ),
                            justify="between",
                            width="100%",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock")),
                            placeholder="Enter your password",
                            id="password",
                            type="password",
                            size="3",
                            width="100%",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.button("Sign in", size="3", width="100%", type_="submit"),
                    on_submit=LoginState.on_submit,
                    ),
                    rx.center(
                        rx.text("New here?", size="3"),
                        rx.link("Sign up", on_click=rx.redirect(REGISTER_ROUTE), size="3"),
                        opacity="0.8",
                        spacing="2",
                        direction="row",
                        width="100%",
                    ),
                    spacing="6",
                    width="100%",
                ),
                max_width="28em",
                size="4",
                width="100%",
            )

def login_component() -> rx.Component:
    login_form = login_default_icons()
    return rx.flex(
                rx.cond(
                    LoginState.is_hydrated,  # type: ignore
                    rx.chakra.vstack(
                        rx.cond(  # conditionally show error messages
                            LoginState.error_message != "",
                            rx.chakra.text(LoginState.error_message),
                        ),
                        login_form,
                        rx.chakra.link("Register", href=REGISTER_ROUTE),
                        padding_top="10vh",
                            ),
                        ),
                            
                    width="100%",
                    direction="column",
                    align="center",
                    justify="center",
                    )