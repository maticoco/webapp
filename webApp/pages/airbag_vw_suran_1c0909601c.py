import reflex as rx
from ..repository.login_state import require_login
from ..components.components import navbar_user, footer, upload, clear_card, color 
from ..repository.base_state import State
from ..repository.upload_state import UploadState
from ..routes import AIRBAG_VW_SIEMENS_1C0909601C
from ..modules.module_list import MODULE3
from ..modules.process_list import PROCESS1
from ..modules.module_img_list import AIRBAG3


@rx.page(route=AIRBAG_VW_SIEMENS_1C0909601C,
         title="Airbags VW Suran Fox SIEMENS 1C0 909 601C", 
         on_load=UploadState.set_config(PROCESS1,MODULE3,AIRBAG3)
         )

def airbag_vw_siemens_1c0909601c() -> rx.Component:
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
