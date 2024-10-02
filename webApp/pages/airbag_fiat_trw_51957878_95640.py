import reflex as rx
from ..repository.login_state import require_login
from ..components.components import navbar_user, footer, upload, clear_card, color 
from ..repository.base_state import State
from ..repository.upload_state import UploadState
from ..routes import AIRBAG_TRW_51957878
from ..modules.module_list import MODULE2
from ..modules.process_list import PROCESS1
from ..modules.module_img_list import AIRBAG2


@rx.page(route=AIRBAG_TRW_51957878,
         title="Airbags Fiat Palio Siena Strada TRW 51957878", 
         on_load=UploadState.set_config(PROCESS1,MODULE2,AIRBAG2)
         )
@require_login
def airbag_fiat_trw_51957878_95640() -> rx.Component:
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
