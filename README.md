# Sistema de Gestión de Carreras Universitarias

Proyecto desarrollado con Django y MariaDB para gestionar carreras universitarias mediante un sistema CRUD.

## Tecnologías utilizadas

- Python 3.13
- Django 5.0.14
- MariaDB 10.4
- XAMPP
- MySQLclient 2.2.8
- Bootstrap 5.3.3
- Git y GitHub

## Funcionalidades

El sistema permite:

- Registrar carreras universitarias.
- Listar carreras registradas.
- Editar carreras.
- Eliminar carreras.
- Validar los datos ingresados.
- Conectarse a una base de datos MariaDB.

## Datos de una carrera

Cada carrera contiene:

- Nombre
- Código
- Facultad
- Duración
- Modalidad
- Jornada
- Arancel
- Cupos
- Correo electrónico

## Estructura del proyecto

```text
universidad_backend/
├── carreras/
│   ├── migrations/
│   ├── templates/
│   │   └── carreras/
│   │       ├── inicio.html
│   │       ├── lista.html
│   │       ├── crear.html
│   │       ├── editar.html
│   │       └── eliminar.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── universidad/
│   ├── settings.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
└── .gitignore