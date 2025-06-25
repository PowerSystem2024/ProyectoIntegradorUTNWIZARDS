# ===== CONFIG.PY =====
# Este archivo es el "cerebro" de la configuración del sistema
# Aquí se definen todas las reglas y configuraciones importantes

# Importamos las herramientas necesarias para manejar variables de entorno
import os
from dotenv import load_dotenv

# Cargamos las variables de entorno desde el archivo .env
# Las variables de entorno son como secretos que guardamos fuera del código
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# ===== CONFIGURACIÓN DE LA BASE DE DATOS =====
# Aquí guardamos la información para conectarnos a la base de datos
# Usamos variables de entorno para mantener segura la información sensible
DB_NAME = os.getenv('DB_NAME', '')  # Nombre de la base de datos
DB_USER = os.getenv('DB_USER', '')  # Usuario de la base de datos
DB_PASSWORD = os.getenv('DB_PASSWORD', '')  # Contraseña de la base de datos
DB_HOST = os.getenv('DB_HOST', '')  # Dirección del servidor
DB_PORT = os.getenv('DB_PORT', '')  # Puerto de conexión

print("DB_PASSWORD:", repr(DB_PASSWORD))

# Guardamos toda la configuración de la base de datos en un diccionario
DB_CONFIG = {
    'dbname': DB_NAME,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'host': DB_HOST,
    'port': DB_PORT
}

# ===== CONFIGURACIÓN DE LA APLICACIÓN =====
# Aquí guardamos las reglas y límites del sistema
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'  # Modo de depuración
MAX_LIBROS_POR_USUARIO = int(os.getenv('MAX_LIBROS_POR_USUARIO', '3'))  # Máximo de libros que puede pedir un usuario
DIAS_PRESTAMO = int(os.getenv('DIAS_PRESTAMO', '15'))  # Días que se puede tener un libro prestado
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')  # Usuario administrador por defecto
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')  # Contraseña administrador por defecto

# Guardamos toda la configuración de la aplicación en un diccionario
APP_CONFIG = {
    'debug': DEBUG,
    'max_books_per_user': MAX_LIBROS_POR_USUARIO,
    'loan_days': DIAS_PRESTAMO,
    'admin_username': ADMIN_USERNAME,
    'admin_password': ADMIN_PASSWORD
}

# ===== NIVELES DE USUARIO =====
# Definimos los diferentes tipos de usuarios y sus niveles de acceso
USER_LEVELS = {
    'ADMIN': 1,    # Administrador: acceso total al sistema
    'STAFF': 2,    # Personal: puede gestionar préstamos y libros
    'USER': 3      # Usuario normal: puede pedir libros prestados
}

# ===== ESTADOS DE PRÉSTAMO =====
# Definimos los diferentes estados que puede tener un préstamo
LOAN_STATUS = {
    'PENDING': 'pendiente',    # Préstamo solicitado pero no aprobado
    'APPROVED': 'activo',      # Préstamo aprobado y en curso
    'REJECTED': 'rechazado',   # Préstamo rechazado
    'RETURNED': 'devuelto',    # Libro devuelto
    'OVERDUE': 'vencido'       # Préstamo vencido
}

# ===== ESTADOS DE LIBRO =====
# Definimos los diferentes estados que puede tener un libro
BOOK_STATUS = {
    'AVAILABLE': 'disponible',  # Libro disponible para préstamo
    'RESERVED': 'reservado',    # Libro reservado por alguien
    'BORROWED': 'prestado'      # Libro actualmente prestado
} 