# Requisitos Técnicos y Guía de Instalación (Versión Dockerizada)

## 1. Requisitos Mínimos de Software y Hardware

### Hardware
- Procesador: Intel/AMD 1 GHz o superior
- Memoria RAM: 2 GB mínimo (4 GB recomendado)
- Espacio en disco: 500 MB libres para el sistema, dependencias y volúmenes de datos
- Resolución de pantalla: 1024x768 o superior

### Software
- Sistema Operativo: Windows 10/11, Linux o MacOS
- Docker Desktop (recomendado última versión): https://www.docker.com/products/docker-desktop/
- (Opcional) Visual Studio Code u otro editor de texto

## 2. Estructura de Contenedores

- **Contenedor de base de datos**: PostgreSQL 12, persistente mediante volumen Docker, solo accesible internamente.
- **Contenedor de aplicación**: Python 3.9, con dependencias instaladas, acceso interactivo por terminal.
- **Red interna Docker**: Comunicación segura entre app y base de datos.
- **Persistencia**: Los datos de la base se mantienen aunque se detenga o elimine el contenedor.

## 3. Archivos necesarios
- `docker-compose.yml` (orquestación de contenedores)
- `Dockerfile` (construcción de la imagen de la app)
- `requirements.txt` (dependencias Python)
- `.env` (variables de entorno, credenciales y configuración)
- `documentacion/estructura_biblioteca.sql` (estructura de la base de datos)
- Código fuente Python del sistema

## 4. Instalación y uso

### 4.1. Clona el repositorio o copia los archivos en una carpeta local.

### 4.2. Configura el archivo `.env` con tus datos:
```
DB_NAME=biblioteca_myne
DB_USER=MyneSolutions
DB_PASSWORD=c5Rnoxm9bgdJF
DB_HOST=db
DB_PORT=5432
```

### 4.3. Construye y levanta los contenedores:
```bash
docker-compose up --build -d
```

### 4.4. Accede a la aplicación de consola:
```bash
docker exec -it biblioteca_app bash
# Dentro del contenedor:
python main.py
```

### 4.5. (Opcional) Accede a la base de datos:
```bash
docker exec -it biblioteca_db psql -U MyneSolutions -d biblioteca_myne
```

### 4.6. Detén los contenedores:
```bash
docker-compose down
```

### 4.7. Elimina todo (incluyendo datos de la base):
```bash
docker-compose down -v
```

## 5. Desarrollo y persistencia
- El código fuente está mapeado como volumen, por lo que los cambios en tu PC se reflejan en el contenedor.
- Los datos de la base de datos persisten en el volumen `postgres_data`.
- Puedes entrar y salir del contenedor de la app las veces que quieras para pruebas y desarrollo.

## 6. Notas y recomendaciones
- No es necesario instalar dependencias Python en tu máquina local, solo dentro del contenedor.
- La base de datos solo es accesible desde la red interna de Docker, no desde el exterior.
- Si necesitas exponer la base para administración, puedes agregar temporalmente el mapeo de puerto 5432 en `docker-compose.yml`.
- Para producción, considera usar Docker Secrets o variables de entorno del sistema para mayor seguridad.
- Si cambias el `Dockerfile` o `requirements.txt`, recuerda reconstruir la imagen con `docker-compose up --build -d`.

---

¿Dudas o problemas? Consulta los logs con:
```bash
docker logs biblioteca_app
```
y
```bash
docker logs biblioteca_db
``` 