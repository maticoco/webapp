FROM caddy:2

# Copy static files from the app container to the Caddy container
COPY --from=local/reflex-app /app/.web/_static /srv

# Add the Caddyfile
ADD Caddyfile /etc/caddy/Caddyfile
