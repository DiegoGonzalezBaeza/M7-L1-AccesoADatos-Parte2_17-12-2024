# M7-L1-AccesoADatos-Parte2_17-12-2024
Proyecto educativo

# Hotel Management System

Este proyecto es una aplicación básica de gestión de hotel desarrollada con **Django** y **PostgreSQL**. Proporciona funcionalidades para mostrar habitaciones disponibles y listas de huéspedes.

## Contenido

1. [Características](#características)
2. [Requisitos](#requisitos)
3. [Configuración del Proyecto](#configuración-del-proyecto)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Endpoints](#endpoints)
6. [Plantillas](#plantillas)
7. [Administración](#administración)
8. [Uso](#uso)

---

## Características

- **Modelos Django**: Definidos para gestionar **Guest** y **Room**.
- **Consultas SQL Crudas**: Dos vistas incluyen consultas directas a la base de datos.
- **Plantillas HTML**: Páginas para mostrar la lista de huéspedes y habitaciones disponibles.
- **Administración**: Configurado con el panel de administración de Django.

---

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener lo siguiente instalado:

- **Python 3.8+**
- **Django 4.x**
- **PostgreSQL** con una base de datos configurada
- **pip** y **virtualenv** (opcional pero recomendado)

---

## Configuración del Proyecto

### 1. Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd <directorio-del-proyecto>
```

### 2. Crear un entorno virtual

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si no tienes un archivo `requirements.txt`, puedes generarlo con:
> ```bash
> pip freeze > requirements.txt
> ```

### 4. Configurar la base de datos

Edita el archivo **settings.py** para conectar PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Hotel_DB',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Crea la base de datos **Hotel_DB** en PostgreSQL antes de continuar.

### 5. Migraciones

Ejecuta las migraciones para crear las tablas en la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear un superusuario (opcional)

Para acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```

---

## Estructura del Proyecto

```plaintext
hotel_management/
│
├── hotel/
│   ├── migrations/             # Migraciones de la base de datos
│   ├── templates/              # Plantillas HTML
│   │   ├── guests.html
│   │   ├── guests_DB.html
│   │   ├── rooms.html
│   │   └── rooms_DB.html
│   ├── admin.py                # Registro de modelos en el admin
│   ├── models.py               # Definición de modelos (Guest, Room)
│   ├── views.py                # Lógica de vistas
│   └── urls.py                 # Rutas de la aplicación
│
├── manage.py                   # Comando para ejecutar Django
└── requirements.txt            # Dependencias
```

---

## Endpoints

### Habitaciones Disponibles

1. **Base de Datos Directa**:
   - URL: `/available_rooms_DB/`
   - Vista: `available_rooms_base_de_datos`

2. **Con ORM**:
   - URL: `/available_rooms/`
   - Vista: `available_rooms`

### Lista de Huéspedes

1. **Base de Datos Directa**:
   - URL: `/guest_list_DB/`
   - Vista: `guest_list_base_de_datos`

2. **Con ORM**:
   - URL: `/guest_list/`
   - Vista: `guest_list`

---

## Plantillas

Las plantillas HTML se encuentran en **hotel/templates/**:

- **guests.html**: Lista de huéspedes con ORM.
- **guests_DB.html**: Lista de huéspedes con SQL crudo.
- **rooms.html**: Habitaciones disponibles con ORM.
- **rooms_DB.html**: Habitaciones disponibles con SQL crudo.

---

## Administración

Para acceder al panel de administración de Django:

1. Ejecuta el servidor local:

   ```bash
   python manage.py runserver
   ```

2. Ingresa a `http://127.0.0.1:8000/admin/` y usa tus credenciales de superusuario.

3. Desde el panel, puedes gestionar las entidades **Guest** y **Room**.

---

## Uso

1. Ejecutar el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

2. Accede a las rutas en tu navegador:

   - Habitaciones disponibles (SQL crudo): `http://127.0.0.1:8000/available_rooms_DB/`
   - Habitaciones disponibles (ORM): `http://127.0.0.1:8000/available_rooms/`
   - Lista de huéspedes (SQL crudo): `http://127.0.0.1:8000/guest_list_DB/`
   - Lista de huéspedes (ORM): `http://127.0.0.1:8000/guest_list/`

---

## Próximos Pasos

- **Autenticación**: Añadir autenticación de usuarios.
- **Mejora de UI/UX**: Mejorar las plantillas con CSS y frameworks como Bootstrap.
- **Optimización de Consultas**: Evitar consultas SQL crudas y usar ORM para mayor seguridad.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir:

1. Haz un fork del proyecto.
2. Crea una nueva rama.
3. Envía un pull request.

---

## Licencia

Este proyecto está bajo la licencia MIT.
