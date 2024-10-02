import reflex as rx
from ..repository.login_state import require_login
from ..components.components import navbar_user, footer, upload, clear_card, color 
from ..repository.base_state import State
from ..repository.upload_state import UploadState
from ..routes import AIRBAG_AUTOLIV_62XXXXXXX
from ..modules.module_list import MODULE4
from ..modules.process_list import PROCESS1
from ..modules.module_img_list import AIRBAG4


@rx.page(route=AIRBAG_AUTOLIV_62XXXXXXX,
         title="Airbags PSA Autoliv 95320", 
         on_load=UploadState.set_config(PROCESS1,MODULE4,AIRBAG4)
         )
@require_login
def airbag_psa_autoliv_95320() -> rx.Component:
    return rx.box(
        navbar_user(),
        rx.hstack(
            upload(),
            clear_card(),
            width="100%",
            justify="between",
            height="43em",
            padding="3em",
        ),
        footer(),
        bg=rx.color(color, 2),
    )
