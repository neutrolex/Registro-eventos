## 📄 Descripción del Proyecto

Este proyecto es una aplicación web desarrollada con Django para la gestión eficiente de eventos. Permite a los usuarios realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre eventos, facilitando el registro, edición y eliminación de actividades programadas. El sistema está diseñado para ser intuitivo y seguro, asegurando la validación de datos y el control de acceso.

**Integrantes:**  
- Zaith Saenz - Developer  
- Yordy Campo - Developer

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

## 🧾 Historia de Usuario: Registro de Eventos

**Como** administrador del sistema,  
**quiero** registrar eventos con su fecha, ubicación y organizador,  
**para** llevar un control ordenado de las actividades programadas.

### ✅ Criterios de Aceptación

- El usuario puede crear, ver, editar y eliminar eventos.
- Los eventos incluyen: nombre, fecha, ubicación y organizador.
- La fecha debe ser válida y futura.
- Todos los campos son obligatorios.
- Validación de datos en frontend y backend.
- Los eventos se muestran en una tabla con opción de búsqueda y orden por fecha.

---

## 📋 Checklist de Tareas

### Frontend
- Crear formulario con campos: nombre, fecha, ubicación, organizador.
- Validar que ningún campo esté vacío.
- Validar que la fecha no sea anterior al día actual.
- Mostrar mensajes de error en tiempo real.
- Implementar tabla/lista para visualizar eventos.
- Agregar botones: Editar, Eliminar, Registrar evento.
- Implementar paginación y búsqueda por nombre o fecha.
- Mostrar notificaciones tras operaciones exitosas.

### Backend
- Crear modelo Evento con los campos requeridos.
- Crear endpoints CRUD: GET, POST, PUT, DELETE.
- Validar que la fecha del evento sea futura.
- Validar que todos los campos estén presentes y correctos.
- Implementar paginación y filtros por fecha y nombre.
- Guardar eventos en la base de datos.
- Implementar control de errores y respuestas apropiadas.
- Autenticar que solo usuarios autorizados puedan registrar o eliminar eventos.