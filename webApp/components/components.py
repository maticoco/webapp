import reflex as rx
from reflex.style import toggle_color_mode
from ..styles.styles import style_notify,Size
from ..repository.base_state import State
from ..repository.registration import RegistrationState
from ..repository.upload_state import UploadState
from ..repository.login_state import require_login, LoginState
from ..repository.users_state import UserState
from ..routes import GOLMM_ROUTE, LOGIN_ROUTE , REGISTER_ROUTE, AIRBAG_00521545140, AIRBAG_TRW_51957878,AIRBAG_VW_SIEMENS_1C0909601C,AIRBAG_AUTOLIV_62XXXXXXX,CELTA_BCM_PINCODE
from ..modules.module_img_list  import  DASH1,AIRBAG1,AIRBAG2,AIRBAG3,AIRBAG4,BCM1                                                                              
from ..model.user import User
from ..model.auth_session import AuthSession


from ..styles.styles import color , accent_color, Size


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
                rx.desktop_only(
                    rx.hstack(
                        heading_component(),
                        rx.hstack(
                            navbar_link("Home", "/#"),
                            navbar_link("Sobre Nosotros", "/about"),
                            navbar_link("Calculadoras", "/calcs"),
                            navbar_link("Contacto", "/#"),
                            spacing="5",
                            justify="between" 
                            ),
                            rx.spacer(),
                            username(),                                   
                            user_menu(),
                            rx.vstack(
                                dark_light_theme(),                            
                                login_menu_desktop(),    
                                padding=Size.DEFAULT.value,
                                align="end" 
                            ),                     
                            
                            align="center",
                            padding_x=Size.DEFAULT.value,
                            padding_bottom=Size.SMALL.value,
                            witdh="100%"
                            ),
                            
                        ),
                rx.mobile_and_tablet(
                    rx.hstack(
                        rx.hstack(
                            rx.image(
                                src="/logo_cerrajeria.png",
                                width=Size.SUPERBIG.value,
                                height="auto",
                                border_radius="25%",
                                    ),
                                    margin=Size.SMALL.value,
                                    align_items="center",
                                ),
                                rx.spacer(),
                                username(),
                                user_menu(),
                                menu_movile(),
                                padding=Size.SMALL.value
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

def heading_component()-> rx.Component:
    return rx.hstack(
                rx.image(
                    src="/logo_cerrajeria.png",
                    width=Size.SUPERBIG.value,
                    height="auto",
                    border_radius="25%",
                    ),
                rx.heading(
                    "Cerrajeria Automotriz", size="7", weight="bold",color_scheme=color
                    ),
                justify="start",    
                align_items="center",
                padding=Size.DEFAULT.value
                ),
    
def username()-> rx.Component:
    return rx.heading(
                    State.authenticated_user.username, size="7", weight="bold",color_scheme=color
                    )

def image_component()-> rx.Component:
    return rx.flex(rx.scroll_area(
            rx.image(src='/background.jpg',padding=Size.BIG.value),
            width="100%",
            height="100%",
            direction="column",
            align="center",
            justify="center",            
            ),
            width="100%",
            style={"height": "100%"},
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
                            height="100%",
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
                    rx.cond(State.is_authenticated == False,
                    rx.menu.item("Log in",on_click=rx.redirect(LOGIN_ROUTE))),
                    rx.cond(State.is_authenticated == False,
                    rx.menu.item("Sign up",on_click=rx.redirect(REGISTER_ROUTE))),
                    rx.menu.separator(),
                    rx.menu.item("Log out",on_click=State.do_logout),
                    bg=rx.color(color, 2),
                ),
                justify="end",
            ),
          
def menu_movile() -> rx.Component:
    return  rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home",on_click=rx.redirect("/#")),
                        rx.menu.item("Sobre Nosotros",on_click=rx.redirect("/about")),
                        rx.menu.item("Calculadoras",on_click=rx.redirect("/calcs")),
                        rx.menu.item("Contacto",on_click=rx.redirect("/#")),
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
    return rx.box(
                rx.scroll_area(
                rx.grid(
                cards_modules(img=DASH1,text="Gol G6 ",strong="Magnetti Marelli Nec + 95320",route=GOLMM_ROUTE),
                cards_modules(img=AIRBAG1,text="FIAT Cronos/Argo/Strada 2023-> ",strong="MOPAR A3C07434303 0052154140", route=AIRBAG_00521545140),
                cards_modules(img=AIRBAG2,text="FIAT Palio/Siena/Strada Novo >2013-2018< ",strong="TRW 00051957878", route=AIRBAG_TRW_51957878),
                cards_modules(img=AIRBAG3,text="VW Suran/Fox >2005-2011< ",strong="SIEMENS_1C0909601C", route=AIRBAG_VW_SIEMENS_1C0909601C),
                cards_modules(img=AIRBAG4,text="Peugeot 308/408 >2011-2015< ",strong="AUTOLIV 6202260800", route=AIRBAG_AUTOLIV_62XXXXXXX),
                cards_modules(img=BCM1,text="Chevrolet Celta Pincode remote >2010-2015< ",strong="GM 52034351 -> 9S12256", route=CELTA_BCM_PINCODE),
                # spacing="4",
                # columns="3",
                # gap="1rem",
                # width= "100%",
                
                gap="1rem",
                grid_template_columns=[
                    "1fr",
                    "repeat(2, 1fr)",
                    "repeat(2, 1fr)",
                    "repeat(3, 1fr)",
                    "repeat(4, 1fr)",
                ],
                width="100%",
                ),
                
                )
                
            )

def cards_modules(img: str, text: str , strong: str, route: str)-> rx.Component:
    return rx.card(
                        rx.inset(
                            rx.image(
                                src=img,
                                padding="0.5em",
                                height="200px",
                                width="auto",                                
                                border_radius="15px 50px",
                                border="5px solid #555",
                            ),
                            side="top",
                            pb="current",
                        ),
                        rx.text(
                            text,rx.text.strong((strong),as_="label",                           
                        ),
                        
                    ),
                    rx.button("Load Dump", size="3",on_click=rx.redirect(route)),
                    width="20em",
                    height="20em"
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
                padding_top=Size.SMALL.value,
            ),
        ),
        
    )

def about_component()-> rx.Component:
    return rx.scroll_area(
                rx.flex(
                    rx.text(
                        """Con más de 30 años de experiencia, nuestra empresa comenzó en 1994 como una pequeña cerrajería.
                          A lo largo del tiempo, hemos evolucionado para adaptarnos a los cambios en el sector automotor, invertiendo en tecnología y capacitación para ofrecer servicios de corte de llaves, sistemas inmobilizadores, inyección electrónica, airbag, ABS y tableros digitales, así como programación. Contamos con herramientas de última generación para asegurar la precisión y eficiencia en nuestros trabajos. Nuestra meta ha sido siempre trabajar de manera responsable y brindar resultados de alta calidad. Agradecemos el apoyo de nuestros clientes y seguimos comprometidos con nuestra visión de principio.""",
                    ),
                    direction="column",
                    spacing="6",
                    padding=Size.SUPERBIG.value
                    
                ),
                type="always",
                scrollbars="vertical",
                style={"height": "100%"},
                
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
        rx.scroll_area(
        rx.image(src=UploadState.img),
        rx.text(UploadState.decoded_data,white_space="pre"),
        ),
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

def clear_card() -> rx.Component:
    return rx.card(
        rx.scroll_area(
        rx.text(UploadState.decoded_data),
        rx.text(UploadState.modified_filename),
        rx.image(src=UploadState.img),
        rx.cond(
            UploadState.show_download_button,
            rx.button(
                "Descargar archivo modificado", 
                on_click=rx.download(rx.get_upload_url(UploadState.modified_filename))
            ),
            rx.text(f"Cargue aqui el DUMP")
            
            ),
        ),
        padding=Size.BIG.value,
        size="5",
        border=f"1px solid {color}",
        width="100%",
        height="100%"
    )

def table_user(list_user: list[User])-> rx.Component:
    return rx.table.root(
       rx.table.header(
           rx.table.row(
               rx.table.column_header_cell('UserID'),
               rx.table.column_header_cell('Username'),               
               rx.table.column_header_cell('Whitelist'),

               
           )
       ),
       rx.table.body(
            rx.foreach(list_user, row_table)
       ) 
    )

def row_table(user: User)-> rx.Component:
    return rx.table.row(
        rx.table.cell(user.id),
        rx.table.cell(user.username),
        rx.table.cell(user.enabled),

        
        rx.table.cell(rx.hstack(            
            delete_user_dialogo_component(user.username)
        ))
    )

def search_user_component() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder='Ingrese usuario', on_change=UserState.search_on_change),
        rx.button ('Buscar Usuario' , on_click= UserState.get_user_by_username)
    )

def create_user_form()-> rx.Component:
    return rx.form(
                rx.vstack(
                    rx.input(
                        placeholder='Nombre de usuario',
                        name= 'username'
                    ),
                    rx.input(
                        placeholder='Email',
                        name= 'Email'
                    ),
                    rx.input(
                        placeholder='Contraseña',
                        name= 'password',
                        type='password'
                    ),
                    
                    rx.dialog.close(
                        rx.button('Guardar', type='submit')
                    ),
                ),
                on_submit=UserState.create_user,
    )

def create_user_dialogo_componenet() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button('Crear Usuario') ),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title('Crear Usuario'),
                #create_user_form(),
                singup_component(),
                justify='center',
                align='center',
                direction='column',
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button('Cancelar', color_scheme='gray', variant= 'soft')
                ),
                spacing='3',
                margin_top=Size.DEFAULT.value,
                justify='end',
            ),
            style={'width': '600px'}
        ),
    )

def delete_user_dialogo_component(username: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon('trash-2'))),
        rx.dialog.content(
            rx.dialog.title('Eliminar usuario'),
            rx.dialog.description('Esta seguro de querer eliminar el usuario '+ username),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        'Cancelar',
                        color_scheme='gray',
                        variant='soft'
                    ),
                ),
                rx.dialog.close(
                    rx.button('Confirmar', on_click=UserState.delete_user(username)),    
                ),

                spacing='3',
                margin_top='16px',
                justify='end',
            )
        )
    )

def notify_component(message: str, icon_notify: str, color: str) -> rx.Component:
    return rx.callout(
        message,
        icon=icon_notify,
        style=style_notify,
        color_scheme=color
    )