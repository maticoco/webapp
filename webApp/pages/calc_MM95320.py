import reflex as rx
from ..repository.login_state import require_login
from ..components.components import navbar_user, footer, upload, result_card, color 
from ..repository.base_state import State
from ..repository.upload_state import UploadState
from ..routes import GOLMM_ROUTE
from ..modules.process_list import PROCESS2
from ..modules.module_img_list import DASH1




@rx.page(route=GOLMM_ROUTE,
         title="GOL G6 MM95320", 
         on_load=UploadState.set_config(PROCESS2,"",DASH1)
         )



def calc_mm95320() -> rx.Component:
    
    return rx.box(            
            navbar_user(),
            rx.hstack(           
                upload(),
                result_card(),
                width= "100%",
                justify="between",                
                height="43em",
                padding="3em",
                ), 
            footer(),
          
            bg=rx.color(color, 2),
            ) 
