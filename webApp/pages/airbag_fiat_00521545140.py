import reflex as rx
from ..repository.login_state import require_login
from ..components.components import navbar_user, footer, upload, clear_card, color 
from ..repository.base_state import State
from ..repository.upload_state import UploadState
from ..routes import AIRBAG_00521545140
from ..modules.module_list import MODULE1
from ..modules.process_list import PROCESS1
from ..modules.module_img_list import AIRBAG1

@rx.page(route=AIRBAG_00521545140,
         title="Airbags Fiat Argo Cronos Strada AIRBAG_00521545140", 
         on_load=UploadState.set_config(PROCESS1,MODULE1,AIRBAG1)
         )
@require_login
def fiat_airbag_00521545140() -> rx.Component:
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
