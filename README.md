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
## Panel de administración

1. Aplicar migraciones: `python manage.py migrate`
2. Crear superusuario: `python manage.py createsuperuser`
3. Iniciar el servidor: `python manage.py runserver`
4. Entrar a `http://127.0.0.1:8000/admin/` y cargar posts desde la sección Posts.
## CRUD de posts e imágenes

Desde el sitio se pueden crear, ver, editar y eliminar posts:

- Listado: `/posts/`
- Crear: `/posts/crear/`
- Detalle: `/posts/<slug>/`
- Editar: `/posts/<slug>/editar/`
- Eliminar (con página de confirmación): `/posts/<slug>/eliminar/`

### Manejo de imágenes

- El modelo `Post` tiene un campo `imagen` (`ImageField`, opcional) que guarda los archivos en `media/posts/`.
- En `settings.py` se configuraron `MEDIA_URL = "/media/"` y `MEDIA_ROOT = BASE_DIR / "media"`.
- En `blog_project/urls.py` se sirven los archivos media mientras `DEBUG` está activo.
- Los formularios usan `enctype="multipart/form-data"` y las vistas reciben `request.FILES`.

### Nueva dependencia

Se instaló **Pillow** (necesaria para `ImageField`): `pip install -r requirements.txt`.

### Cómo probar la carga de imágenes

1. Aplicar migraciones: `python manage.py migrate`
2. Iniciar el servidor: `python manage.py runserver`
3. Entrar a `http://127.0.0.1:8000/posts/crear/`, completar el formulario y elegir una imagen.
4. Abrir el detalle del post para ver la imagen.