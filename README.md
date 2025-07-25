## 📄 Descripción del Proyecto

Este proyecto es una aplicación web desarrollada con Django para la gestión eficiente de eventos. Permite a los usuarios realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre eventos, facilitando el registro, edición y eliminación de actividades programadas. El sistema está diseñado para ser intuitivo y seguro, asegurando la validación de datos y el control de acceso.

**Integrantes:**

- Christofer Salas - Scrum Master
- Cesar Cabrejos - Product Owner
- Zaith Saenz - Developer 1
- Yordy Campo - Developer 2
- Anthony Ramos - Developer 3

---

# 📘 Guía Rápida de Instalación y Ejecución

Sigue estos pasos para instalar y ejecutar el proyecto en tu entorno local.

## 🚀 Requisitos

- Python 3.10 o superior
- Git
- Visual Studio Code (opcional)

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/usuario/nombre-del-repositorio.git
```

## 2️⃣ Abrir el proyecto en Visual Studio Code

- Abre Visual Studio Code.
- Ve a **Archivo > Abrir carpeta...** y selecciona la carpeta del proyecto.

## 3️⃣ Crear y activar entorno virtual

```bash
python -m venv venv
.\venv\Scripts\activate
```

## 4️⃣ Instalar dependencias

```bash
pip install django
```

## 5️⃣ Verificar instalación

```bash
python --version
django-admin --version
```

## 6️⃣ Ejecutar el servidor

```bash
python manage.py runserver
```

Abre tu navegador y visita [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

.
🧾 Historia de Usuario: Registro de Eventos
🏷️ Etiquetas:
#eventos #registro #frontend #backend #formulario #CRUD

📝 Descripción:
Como administrador del sistema, quiero registrar eventos con su fecha, ubicación y organizador, para llevar un control ordenado de las actividades programadas en el sistema.

✅ Criterios Clave de Aceptación:
El usuario puede crear, ver, editar y eliminar eventos.

Los eventos deben incluir: nombre del evento, fecha, ubicación, y organizador.

La fecha debe ser válida y futura (no fechas pasadas).

Todos los campos son obligatorios.

El sistema debe validar datos en frontend y backend.

Los eventos deben mostrarse en una tabla o listado con opción de búsqueda.

El sistema debe permitir ordenar los eventos por fecha.

📋 Checklist de Tareas
Frontend
Crear formulario con inputs: nombre, fecha, ubicación, organizador.

Validar que ningún campo esté vacío.

Validar que la fecha no sea anterior al día actual.

Mostrar mensajes de error en tiempo real.

Implementar tabla o lista para visualizar eventos registrados.

Agregar botones: Editar, Eliminar, y Registrar evento.

Implementar paginación y búsqueda por nombre o fecha.

Mostrar notificación o alerta tras una operación exitosa (registro, edición, eliminación).

Backend
Crear modelo Evento con campos: nombre, fecha, ubicacion, organizador.

Crear endpoints RESTful: GET, POST, PUT, DELETE para eventos.

Validar que la fecha del evento sea futura.

Validar que todos los campos estén presentes y tengan formato correcto.

Implementar lógica de paginación y filtros por fecha y nombre.

Guardar eventos en base de datos.

Implementar control de errores y respuestas apropiadas (status codes).

Autenticar que solo usuarios autorizados puedan registrar o eliminar eventos.
