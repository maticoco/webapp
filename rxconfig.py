import reflex as rx

config = rx.Config(
    # Nombre de la aplicación (debe coincidir con el nombre del directorio raíz de la app).
    app_name="webApp",

    # URL del backend al que el frontend se conectará.
    api_url="https://back.cerrajerialjr.com.ar",

    # URL donde está desplegado el frontend.
    deploy_url="https://cerrajerialjr.com.ar",

    # Puerto y host del backend en Docker.
    backend_port=8000,
    backend_host="0.0.0.0",

    # Puerto del frontend en desarrollo local (opcional, útil para debug).
    frontend_port=3000,

    # Configuración de CORS (Permitir conexiones desde el dominio del frontend).
    cors_allowed_origins=["https://cerrajerialjr.com.ar"],

    # Configuración de Redis para manejar el estado en el backend.
    redis_url="redis://localhost:6379",

    # Tiempo de espera para solicitudes largas.
    timeout=120,

    # Habilitar compresión para Next.js en el frontend.
    next_compression=True,

    # Desactivar telemetría (opcional).
    telemetry_enabled=False
)
