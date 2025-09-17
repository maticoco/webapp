import reflex as rx

config = rx.Config(
    app_name="webApp",
    api_url="https://back.cerrajerialjr.com.ar",
    db_url="sqlite:///reflex.db",
    backend_host = "0.0.0.0",
    cors_allowed_origins = [
        "https://cerrajerialjr.com.ar",
        "https://www.cerrajerialjr.com.ar",
        "http://localhost:3000",  # Para desarrollo
    ]
    
)
