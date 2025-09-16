# This Dockerfile is used to deploy a single-container Reflex app instance
# to services like Render, Railway, Heroku, GCP, and others.

# It uses a reverse proxy to serve the frontend statically and proxy to backend
# from a single exposed port, expecting TLS termination to be handled at the
# edge by the given platform.
FROM python:3.11

# Instala Caddy server dentro de la imagen
RUN apt-get update -y && apt-get install -y caddy && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el contexto local al contenedor (según .dockerignore)
COPY . .

# Instala los requisitos de la aplicación y Reflex dentro del contenedor
RUN pip install -r requirements.txt

# Despliega las plantillas y prepara la aplicación
RUN reflex init

# Exporta el frontend y lo mueve al directorio de Caddy para ser servido
RUN reflex export --frontend-only --no-zip --loglevel debug && mv .web/_static/* /srv/ && rm -rf .web

# Copia el Caddyfile al contenedor
COPY Caddyfile /etc/caddy/Caddyfile

# Define la señal para detener el contenedor
STOPSIGNAL SIGKILL

# Expone el puerto configurado
EXPOSE $PORT

# # Ejecuta las migraciones y luego inicia Caddy junto con el backend de Reflex
# CMD [ -d alembic ] && reflex db migrate; \
#     caddy start --config /etc/caddy/Caddyfile && reflex run --env prod --backend-only --loglevel debug \
    

# Apply migrations before starting the backend.
CMD [ -d alembic ] && reflex db migrate; \
    caddy start --config /etc/caddy/Caddyfile && redis-server --daemonize yes\
    exec reflex run --env prod --backend-only