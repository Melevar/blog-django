# Blog Django

Proyecto base de un blog web desarrollado con Django.

## Descripción

Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog.
Incluye la configuración base del proyecto y una aplicación llamada `posts`.

## Instalación

Clonar el repositorio:
```bash
git clone https://github.com/Melevar/blog-django.git
```

Entrar a la carpeta del proyecto:
```bash
cd blog-django
```

Crear entorno virtual:
```bash
python -m venv venv
```

Activar entorno virtual:

En Windows PowerShell:
```bash
.\venv\Scripts\Activate.ps1
```

En Linux o macOS:
```bash
source venv/bin/activate
```

Instalar dependencias:
```bash
pip install -r requirements.txt
```

Ejecutar el servidor:
```bash
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000/ 
## Aplicaciones

- **posts**: aplicación inicial para manejar las publicaciones del blog.