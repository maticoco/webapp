#!/bin/bash

# Descargar el proxy si no está ya descargado
if [ ! -f ./cloud_sql_proxy ]; then
  echo "Downloading Cloud SQL Proxy..."
  curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64
  chmod +x cloud_sql_proxy
fi

# Iniciar el proxy de Google Cloud SQL
./cloud_sql_proxy -instances="lithe-record-429615-b8:southamerica-east1:ljr-app"=tcp:5432 &

# Esperar unos segundos para asegurarse de que el proxy esté funcionando
sleep 5

# Iniciar la aplicación Reflex
reflex run --env prod
