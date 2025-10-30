#!/bin/bash
# Script de inicialización para MongoDB usando mongoimport

echo "🚀 Iniciando configuración de MongoDB..."

# Esperar a que MongoDB esté completamente iniciado
sleep 5

# Importar el archivo JSON usando mongoimport
echo "📥 Importando datos de participants.json..."
mongoimport \
  --host localhost \
  --port 27017 \
  --username admin \
  --password admin123 \
  --authenticationDatabase admin \
  --db migx \
  --collection participants \
  --file /docker-entrypoint-initdb.d/participants.json \
  --jsonArray \
  --drop