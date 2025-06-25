# 🧙‍♂️✨🧙‍♀️ UTN WIZARDS - Sistema de Gestión de Biblioteca

## 📚 Descripción del Proyecto

Este proyecto es un **Sistema de Gestión de Biblioteca** desarrollado en Python, con persistencia en PostgreSQL y completamente dockerizado para facilitar su despliegue, uso y corrección. Permite la gestión completa de usuarios, libros, préstamos, categorías y reportes, todo desde una aplicación de consola con interfaz intuitiva.

### 🎯 Funcionalidades Principales

#### 👑 **Funcionalidades de Administración:**
- **👥 Gestión Completa de Usuarios**: Registro, modificación, activación/desactivación de usuarios
- **📚 Gestión Completa de Libros**: Registro, búsqueda, modificación y eliminación de libros
- **📖 Gestión de Préstamos**: Aprobación, seguimiento y administración de todos los préstamos
- **🏷️ Gestión de Categorías**: Creación, modificación y eliminación de categorías de libros
- **📊 Reportes Avanzados**: Generación de reportes detallados y exportación a CSV
- **⚙️ Configuración del Sistema**: Gestión de parámetros y configuraciones globales

#### 👤 **Funcionalidades de Usuarios Estándar:**
- **🔍 Consultas y Búsqueda**: Búsqueda de libros por autor, categoría, disponibilidad, etc.
- **📖 Solicitud de Préstamos**: Solicitar libros disponibles para préstamo
- **📋 Gestión Personal**: Ver mis préstamos activos y historial personal
- **📜 Historial Personal**: Consultar historial de préstamos por diferentes criterios
- **⚙️ Perfil Personal**: Modificar datos personales y contraseña

## ⚠️ IMPORTANTE: Base de Datos Vacía

**La base de datos se encuentra completamente vacía al iniciar el sistema por primera vez.** Para poder ver y probar todas las funcionalidades del sistema, es necesario cargar datos de prueba:

### 📋 Datos que Necesitas Cargar Manualmente:

1. **👥 Usuarios de Prueba** (además del administrador)
2. **🏷️ Categorías de Libros** (para organizar los libros)
3. **📚 Libros de Prueba** (para poder realizar préstamos)
4. **📖 Préstamos de Ejemplo** (para probar reportes)

### 🔑 Credenciales del Administrador

Para acceder al sistema y configurar los datos iniciales, utiliza las siguientes credenciales:

- **Usuario:** `admin`
- **Contraseña:** `admin123`

**Nota:** Este usuario administrador tiene acceso completo a todas las funcionalidades del sistema y es el único usuario que existe por defecto.

## 🛠️ Requisitos del Sistema

- **Sistema Operativo:** Windows 10/11, Linux o MacOS
- **Docker Desktop:** Última versión recomendada ([descargar aquí](https://www.docker.com/products/docker-desktop/))
- **(Opcional) Editor de texto:** Visual Studio Code, PyCharm, etc.

## 📁 Estructura del Proyecto

```
├── documentacion/
│   └── estructura_biblioteca.sql   # Script SQL para crear la estructura de la base de datos
├── Descargas Sistema/              # Carpeta para archivos exportados por la app
├── .env.example                    # Ejemplo de archivo de configuración de entorno
├── docker-compose.yml              # Orquestador de contenedores
├── Dockerfile                      # Imagen de la app Python
├── requirements.txt                # Dependencias Python
├── main.py                         # Código principal de la app
├── database.py                     # Gestión de base de datos
├── models.py                       # Modelos de datos
├── config.py                       # Configuración del sistema
├── utils.py                        # Utilidades y funciones auxiliares
└── README.md                       # Este archivo
```

## 🚀 Configuración Inicial

### 1. Preparación del Entorno

1. **Clona o descarga el proyecto en una carpeta local.**
2. **Copia el archivo `.env.example` a `.env` y edítalo si es necesario:**
   ```
   DB_NAME=biblioteca_myne
   DB_USER=MyneSolutions
   DB_PASSWORD=c5Rnoxm9bgdJF
   DB_HOST=db
   DB_PORT=5432
   ADMIN_USERNAME=admin
   ADMIN_PASSWORD=admin123
   ```

### 2. Levantar el Entorno

1. **Abre una terminal en la carpeta raíz del proyecto.**
2. **Construye y levanta los contenedores:**
   ```bash
   docker-compose up --build -d
   ```
   *(En Ubuntu usa: `docker compose up --build -d`)*

3. **Accede a la aplicación de consola:**
   ```bash
   docker exec -it biblioteca_app bash
   # Dentro del contenedor:
   python main.py
   ```

### 3. Configuración Inicial del Sistema

Una vez que accedas con las credenciales de administrador (`admin` / `admin123`), deberás:

1. **Crear Categorías de Libros:**
   - Ve a "🏷️ Gestión de Categorías"
   - Agrega categorías como: Literatura, Ciencia, Historia, Tecnología, etc.

2. **Registrar Usuarios de Prueba:**
   - Ve a "👥 Gestión de Usuarios"
   - Crea varios usuarios con diferentes niveles (admin, staff, usuario)

3. **Agregar Libros de Prueba:**
   - Ve a "📚 Gestión de Libros"
   - Registra libros con diferentes autores, categorías y estados

4. **Probar Préstamos:**
   - Inicia sesión con usuarios normales
   - Solicita préstamos de libros
   - Prueba las funcionalidades de devolución

## 🎮 Cómo Usar el Sistema

### Para Administradores:
- **Gestión completa de usuarios, libros y categorías**
- **Aprobación de préstamos pendientes**
- **Generación de reportes detallados**
- **Exportación de datos a CSV**

### Para Usuarios Normales:
- **Consulta y búsqueda de libros**
- **Solicitud de préstamos**
- **Visualización de historial personal**
- **Modificación de datos personales**

## 📊 Tipos de Reportes Disponibles

- **Libros más prestados**
- **Usuarios con más préstamos**
- **Libros disponibles vs prestados**
- **Préstamos vencidos por usuario**
- **Historial completo de préstamos**

## 🛑 Cómo Detener y Limpiar el Entorno

- **Detener los contenedores:**
  ```bash
  docker-compose down
  ```
- **Eliminar todo (incluyendo datos de la base):**
  ```bash
  docker-compose down -v
  ```

## 🔧 Notas para el Desarrollo

- El sistema está preparado para desarrollo: los cambios en el código fuente se reflejan automáticamente en el contenedor.
- La base de datos es persistente gracias al volumen Docker.
- La base de datos solo es accesible desde la red interna de Docker.
- Si necesita exponer la base para administración, puede agregar temporalmente el mapeo de puerto 5432 en `docker-compose.yml`.

## 🐛 Solución de Problemas

Si encuentra algún error, consulte los logs con:
```bash
docker logs biblioteca_app
docker logs biblioteca_db
```

## 📝 Ejemplo de Datos de Prueba

### Categorías Sugeridas:
- **Literatura** (CDJ: 800)
- **Ciencia** (CDJ: 500)
- **Historia** (CDJ: 900)
- **Tecnología** (CDJ: 600)
- **Filosofía** (CDJ: 100)

### Usuarios de Prueba:
- **Juan Pérez** (DNI: 12345678) - Usuario normal
- **María García** (DNI: 87654321) - Staff
- **Carlos López** (DNI: 11223344) - Usuario normal

### Libros de Prueba:
- **"Don Quijote"** - Miguel de Cervantes - Literatura
- **"El Principito"** - Antoine de Saint-Exupéry - Literatura
- **"Breve Historia del Tiempo"** - Stephen Hawking - Ciencia

---

## 🎓 Desarrollado por UTN WIZARDS

**¡Gracias por revisar nuestro proyecto!** 

Este sistema de gestión de biblioteca fue desarrollado como proyecto integrador, demostrando las mejores prácticas en desarrollo de software, gestión de bases de datos y containerización con Docker.

---

*Para cualquier consulta o soporte técnico, contactar al equipo de desarrollo.* 
