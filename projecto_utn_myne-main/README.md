# Proyecto Mine Py - Sistema de Gestión de Biblioteca

## Descripción
Este proyecto es un sistema de gestión de biblioteca desarrollado en Python, con persistencia en PostgreSQL y completamente dockerizado para facilitar su despliegue, uso y corrección. Permite la gestión de usuarios, libros, préstamos, categorías y reportes, todo desde una aplicación de consola.

## Requisitos
- **Sistema Operativo:** Windows 10/11, Linux o MacOS
- **Docker Desktop:** Última versión recomendada ([descargar aquí](https://www.docker.com/products/docker-desktop/))
- **(Opcional) Editor de texto:** Visual Studio Code, PyCharm, etc.

## Estructura del proyecto
```
├── documentacion/
│   └── estructura_biblioteca.sql   # Script SQL para crear la estructura de la base de datos
├── Descargas Sistema/              # Carpeta para archivos exportados por la app
├── .env.example                    # Ejemplo de archivo de configuración de entorno
├── docker-compose.yml              # Orquestador de contenedores
├── Dockerfile                      # Imagen de la app Python
├── requirements.txt                # Dependencias Python
├── main.py                         # Código principal de la app
├── database.py, config.py, models.py, utils.py  # Módulos del sistema
└── README.md                       # Este archivo
```

## Configuración inicial
1. **Clona o descarga el proyecto en una carpeta local.**
2. **Copia el archivo `.env.example` a `.env` y edítalo si es necesario:**
   ```
   DB_NAME=biblioteca_myne
   DB_USER=MyneSolutions
   DB_PASSWORD=c5Rnoxm9bgdJF
   DB_HOST=db
   DB_PORT=5432
   ```

## Cómo levantar el entorno
1. **Abre una terminal en la carpeta raíz del proyecto.**
2. **Construye y levanta los contenedores:**
   ```bash
   docker-compose up --build -d
   (en ubuntu corre el comando docker compose up --build -d)
   ```
3. **Accede a la aplicación de consola:**
   ```bash
   docker exec -it biblioteca_app bash
   # Dentro del contenedor:
   python main.py
   ```
4. **(Opcional) Accede a la base de datos:**
   ```bash
   docker exec -it biblioteca_db psql -U MyneSolutions -d biblioteca_myne
   ```

## Cómo detener y limpiar el entorno
- **Detener los contenedores:**
  ```bash
  docker-compose down
  ```
- **Eliminar todo (incluyendo datos de la base):**
  ```bash
  docker-compose down -v
  ```

## Notas para el corrector
- El sistema está preparado para desarrollo: los cambios en el código fuente se reflejan automáticamente en el contenedor.
- La base de datos es persistente gracias al volumen Docker.
- La base de datos solo es accesible desde la red interna de Docker.
- Si necesita exponer la base para administración, puede agregar temporalmente el mapeo de puerto 5432 en `docker-compose.yml`.
- Si encuentra algún error, consulte los logs con:
  ```bash
  docker logs biblioteca_app
  docker logs biblioteca_db
  ```

---
¡Gracias por revisar el proyecto! 
