# ===== MODELS.PY =====
# Este archivo define las "plantillas" de datos que usa el sistema
# Es como un formulario que define qué información guardamos de cada cosa
# También define las clases que usamos para representar los datos en el sistema
# y las operaciones que se pueden realizar sobre ellos.


# ===== IMPORTACIÓN DE LAS HERRAMIENTAS NECESARIAS =====

# Importamos las herramientas necesarias para manejar los datos que usamos en el sistema
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

# ===== MODELO DE USUARIO =====
# Definimos la clase Usuario que representa a un usuario del sistema
# Esta clase define los atributos que tiene un usuario y los métodos que se pueden realizar sobre ellos
# Los atributos son las características que tiene un usuario, como su nombre, contraseña, nivel, etc.
# Los métodos son las acciones que se pueden realizar sobre un usuario, como iniciar sesión, cerrar sesión, etc.
@dataclass
class Usuario:
    """
    Clase que representa a un usuario del sistema.
    Guarda toda la información personal y de acceso de un usuario.
    """
    id: int = 0                    # Número único que identifica al usuario
    nombre: str = ""               # Nombre de usuario para iniciar sesión
    password: str = ""             # Contraseña del usuario
    nivel: str = "usuario"         # Tipo de usuario: admin, staff o usuario normal
    dni: str = ""                  # Número de identificación
    email: str = ""                # Correo electrónico
    telefono: str = ""             # Número de teléfono
    direccion: str = ""            # Dirección física
    fecha_registro: datetime = datetime.now()  # Cuándo se registró
    estado: str = "activo"         # Si está activo o inactivo

    # Método que verifica si el usuario es administrador
    @property
    def es_admin(self) -> bool:
        """Verifica si el usuario es administrador"""
        return self.nivel == "admin"

    # Método que verifica si el usuario es personal de la biblioteca
    @property
    def es_staff(self) -> bool:
        """Verifica si el usuario es personal de la biblioteca"""
        return self.nivel == "staff"

# ===== MODELO DE CATEGORÍA =====
# Definimos la clase Categoria que representa una categoría de libros
# Esta clase define los atributos que tiene una categoría y los métodos que se pueden realizar sobre ellos
# Los atributos son las características que tiene una categoría, como su nombre, descripción, código CDJ, etc.
# Los métodos son las acciones que se pueden realizar sobre una categoría, como agregar una categoría, modificar una categoría, etc.
@dataclass
class Categoria:
    """
    Clase que representa una categoría de libros.
    Ayuda a organizar los libros por temas o materias.
    """
    id: int = 0                    # Número único de la categoría
    nombre: str = ""               # Nombre de la categoría
    descripcion: str = ""          # Descripción detallada
    codigo_cdj: str = ""           # Código de Clasificación Decimal Japonesa

# ===== MODELO DE LIBRO =====
# Definimos la clase Libro que representa un libro en la biblioteca
# Esta clase define los atributos que tiene un libro y los métodos que se pueden realizar sobre ellos
# Los atributos son las características que tiene un libro, como su título, autor, ISBN, código CDJ, etc.
# Los métodos son las acciones que se pueden realizar sobre un libro, como agregar un libro, modificar un libro, etc.
@dataclass
class Libro:
    """
    Clase que representa un libro en la biblioteca.
    Guarda toda la información relevante del libro.
    """
    id: int = 0                    # Número único del libro
    titulo: str = ""               # Título del libro
    autor: str = ""                # Autor o autores
    isbn: str = ""                 # Número ISBN único
    codigo_cdj: str = ""           # Código de clasificación
    categoria_id: int = 0          # ID de la categoría a la que pertenece
    editorial: str = ""            # Editorial que lo publicó
    anio_publicacion: int = 0      # Año de publicación
    estado: str = "disponible"     # Estado: disponible, prestado, reservado
    fecha_registro: datetime = datetime.now()  # Cuándo se registró
    cantidad: int = 1              # Cuántos ejemplares hay
    ubicacion: str = ""            # Dónde está físicamente en la biblioteca
    descripcion: str = ""          # Descripción del contenido

# ===== MODELO DE PRÉSTAMO =====
# Definimos la clase Prestamo que representa un préstamo de un libro a un usuario
# Esta clase define los atributos que tiene un préstamo y los métodos que se pueden realizar sobre ellos
# Los atributos son las características que tiene un préstamo, como el usuario que lo pidió, el libro que se prestó, las fechas de préstamo y devolución, etc.
# Los métodos son las acciones que se pueden realizar sobre un préstamo, como verificar si está vencido, etc.
@dataclass
class Prestamo:
    """
    Clase que representa un préstamo de libro.
    Registra quién pidió el libro, cuándo y su estado.
    """
    id: int = 0                    # Número único del préstamo
    usuario_id: int = 0            # ID del usuario que lo pidió
    libro_id: int = 0              # ID del libro prestado
    fecha_prestamo: datetime = datetime.now()  # Cuándo se prestó
    fecha_devolucion: Optional[datetime] = None  # Cuándo debe devolverse
    fecha_devolucion_real: Optional[datetime] = None  # Cuándo se devolvió realmente
    estado: str = "activo"         # Estado: activo, devuelto, vencido
    observaciones: str = ""        # Notas adicionales

    # Método que verifica si el préstamo está vencido
    @property
    def esta_vencido(self) -> bool:
        return (self.estado == "activo" and 
                self.fecha_devolucion is not None and 
                datetime.now() > self.fecha_devolucion)

# ===== MODELO DE BIBLIOTECA =====
# Definimos la clase Biblioteca que representa la biblioteca en sí
# Esta clase define los atributos que tiene la biblioteca y los métodos que se pueden realizar sobre ellos
# Los atributos son las características que tiene la biblioteca, como los usuarios, libros, préstamos, categorías, etc.
# Los métodos son las acciones que se pueden realizar sobre la biblioteca, como buscar un usuario, un libro, etc.
@dataclass
class Biblioteca:
    """
    Clase que representa la biblioteca en sí.
    Contiene métodos para gestionar libros y préstamos.
    """
    # Inicializamos la biblioteca con listas vacías para los usuarios, libros, préstamos y categorías
    def __init__(self):
        """Inicializa una nueva biblioteca con listas vacías"""
        self.usuarios: List[Usuario] = []      # Lista de usuarios
        self.libros: List[Libro] = []          # Lista de libros
        self.prestamos: List[Prestamo] = []    # Lista de préstamos
        self.categorias: List[Categoria] = []  # Lista de categorías

    # Método que busca un usuario por su nombre
    def buscar_usuario(self, nombre: str) -> Optional[Usuario]:
        """Busca un usuario por su nombre"""
        for usuario in self.usuarios:
            if usuario.nombre.lower() == nombre.lower():
                return usuario
        return None

    # Método que busca un libro por su código CDJ
    def buscar_libro(self, codigo_cdj: str) -> Optional[Libro]:
        """Busca un libro por su código CDJ"""
        for libro in self.libros:
            if libro.codigo_cdj == codigo_cdj:
                return libro
        return None

    # Método que obtiene los préstamos de un usuario específico
    def get_prestamos_usuario(self, usuario_id: int) -> List[Prestamo]:
        """Obtiene los préstamos de un usuario específico"""
        return [p for p in self.prestamos if p.usuario_id == usuario_id]

    # Método que obtiene los libros que están disponibles para préstamo
    def get_libros_disponibles(self) -> List[Libro]:
        """Obtiene los libros que están disponibles para préstamo"""
        return [l for l in self.libros if l.estado == "disponible"]

    # Método que obtiene los préstamos que están vencidos
    def get_prestamos_vencidos(self) -> List[Prestamo]:
        """Obtiene los préstamos que están vencidos"""
        return [p for p in self.prestamos if p.esta_vencido] 