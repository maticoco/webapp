import reflex as rx
from ..repository.login_state import require_login
from ..components.components import navbar_user, footer, upload, result_card, color 
from ..repository.base_state import State
from ..repository.upload_state import UploadState
from ..routes import CELTA_BCM_PINCODE
from ..modules.process_list import PROCESS3
from ..modules.module_img_list import BCM1




@rx.page(route=CELTA_BCM_PINCODE,
         title="Celta BCM Pincode Remote", 
         on_load=UploadState.set_config(PROCESS3,"",BCM1)
         )



def celta_bcm_remote_pincode() -> rx.Component:
    
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
