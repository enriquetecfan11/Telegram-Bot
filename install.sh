#!/bin/bash

# Instalar python3-venv si no está instalado
if ! dpkg -s python3-venv >/dev/null 2>&1; then
    echo "Instalando python3-venv..."
    sudo apt update
    sudo apt install python3-venv -y
fi

# Nombre del entorno virtual
env_name="myenv"

# Crear entorno virtual si no existe
if [ ! -d "$env_name" ]; then
    echo "Creando entorno virtual $env_name..."
    python3 -m venv "$env_name"
fi

# Activar entorno virtual
source "$env_name/bin/activate"

# Instalar los paquetes especificados
echo "Instalando paquetes..."
pip install aiohttp==3.9.1 aiosignal==1.3.1 annotated-types==0.6.0 anyio==3.7.1 APScheduler==3.6.3 async-timeout==4.0.3 attrs==23.1.0 beautifulsoup4==4.12.2 blinker==1.7.0 cachetools==4.2.2 certifi==2023.11.17 cffi==1.16.0 charset-normalizer==3.3.2 click==8.1.7 colorama==0.4.6 deep-translator==1.11.4 distro==1.8.0 exceptiongroup==1.2.0 fastapi==0.104.1 filelock==3.13.1 frozenlist==1.4.0 fsspec==2023.10.0 h11==0.14.0 httpcore==1.0.2 httpx==0.25.2 huggingface-hub==0.19.4 idna==3.6 itsdangerous==2.1.2 Jinja2==3.1.2 MarkupSafe==2.1.3 multidict==6.0.4 openai==1.3.6 outcome==1.3.0.post0 packaging==23.2 Pillow==10.1.0 pycparser==2.21 pydantic==2.5.2 pydantic_core==2.14.5 PySocks==1.7.1 python-telegram-bot==13.7 pytz==2023.3.post1 PyYAML==6.0.1 regex==2023.10.3 requests==2.31.0 schedule==1.2.1 selenium==4.16.0 six==1.16.0 sniffio==1.3.0 sortedcontainers==2.4.0 soupsieve==2.5 SpeechRecognition==3.10.0 sse-starlette==1.6.5 starlette==0.27.0 tiktoken==0.5.1 tokenizers==0.15.0 tornado==6.4 tqdm==4.66.1 trio==0.23.1 trio-websocket==0.11.1 typing_extensions==4.8.0 tzdata==2023.3 tzlocal==5.2 urllib3==2.1.0 uvicorn==0.24.0.post1 Werkzeug==3.0.1 wsproto==1.2.0 yarl==1.9.3 python-dotenv==0.19.2

# Desactivar entorno virtual
deactivate

echo "Instalación completa."
