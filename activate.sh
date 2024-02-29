#!/bin/bash

# Nombre del entorno virtual
env_name="myenv"

# Verificar si el entorno virtual existe
if [ -d "$env_name" ]; then
    # Activar el entorno virtual
    source "$env_name/bin/activate"
    echo "Entorno virtual $env_name activado."
else
    echo "El entorno virtual $env_name no existe."
fi
