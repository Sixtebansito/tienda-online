# Tienda Online (Flask + PostgreSQL)

Una aplicación web desarrollada con Python y Flask que simula una tienda en línea. Permite a los usuarios explorar un catálogo de productos, agregar items a su carrito de compras y realizar pedidos. Además, cuenta con un sistema de administración para gestionar productos (físicos, digitales y perecibles).

## Funcionalidades Principales

- **Catálogo de productos** con visualización de detalles e imágenes personalizadas.
- **Carrito de compras** persistente en sesión.
- **Autenticación** y gestión de usuarios (roles: administrador y cliente).
- **CRUD de productos** (crear, editar, eliminar) protegido por rol de administrador.
- **Polimorfismo** aplicado en la base de datos (Producto Físico, Digital, Perecible) usando SQLAlchemy.

## Capturas de Pantalla

*(Añade aquí tus capturas de pantalla)*

### Catálogo de Productos
![Catálogo](ruta/a/tu/captura-catalogo.png)

### Detalle de Producto
![Detalle](ruta/a/tu/captura-detalle.png)

### Carrito de Compras
![Carrito](ruta/a/tu/captura-carrito.png)

---

## Instrucciones de Instalación y Ejecución

Sigue estos pasos para levantar el proyecto en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone <url-de-tu-repositorio>
cd tienda_online
```

### 2. Crear y activar el entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
```

### 3. Instalar las dependencias
```bash
pip install Flask Flask-SQLAlchemy psycopg2-binary python-dotenv Werkzeug
```

### 4. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto y añade tu configuración de conexión a la base de datos PostgreSQL:
```ini
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta_aqui
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/tienda_db
```

### 5. Ejecutar la base de datos y migraciones (si tienes scripts previos)
Si no has creado las tablas, puedes hacerlo entrando a la consola de python (asegúrate de tener creada la base de datos `tienda_db` en Postgres):
```bash
python
>>> from app import app
>>> from models import db
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

### 6. Ejecutar la aplicación
Ejecuta el siguiente comando (usaremos el puerto 5001 por problemas de conflicto con el 5000 en Mac):
```bash
python app.py
```
Abre tu navegador en: [http://127.0.0.1:5001](http://127.0.0.1:5001)

---

## Credenciales de Prueba

Una vez levantada la aplicación, puedes probar las distintas vistas con los siguientes usuarios (Asegúrate de haberlos registrado primero o que existan en la BD):

- **Usuario Administrador:**
  - **Correo:** admin@admin.com (o tu correo configurado)
  - **Contraseña:** admin123 (o la que hayas elegido)

- **Usuario Cliente:**
  - **Correo:** cliente@cliente.com
  - **Contraseña:** cliente123
