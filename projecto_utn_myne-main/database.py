# =============================================
# EXPLICACIÓN GENERAL DEL ARCHIVO
# =============================================
# Este módulo es fundamental para el sistema de gestión de biblioteca.
# Implementa la clase Database que maneja todas las operaciones CRUD
# (Crear, Leer, Actualizar, Eliminar) para las entidades principales:
# - Usuarios: Gestión de usuarios del sistema
# - Libros: Gestión del catálogo de libros
# - Préstamos: Control de préstamos y devoluciones
# - Categorías: Clasificación de libros
#
# El módulo utiliza PostgreSQL como sistema de gestión de base de datos
# y proporciona una interfaz completa para todas las operaciones
# necesarias en el sistema de biblioteca.
#
# Principales funcionalidades:
# 1. Gestión de usuarios (alta, baja, modificación)
# 2. Gestión de libros (registro, actualización, búsqueda)
# 3. Control de préstamos (registro, devolución, seguimiento)
# 4. Administración de categorías
# 5. Manejo de errores y excepciones de base de datos
# 6. Conexión segura y gestión de sesiones

import psycopg2
from psycopg2.extras import DictCursor
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
from config import DB_CONFIG, APP_CONFIG
from models import Usuario, Libro, Prestamo, Categoria

# =============================================
# EXPLICACIÓN DE LA CLASE DATABASE
# =============================================
# La clase Database es el componente central para la interacción con la base de datos.
# Funciona como una capa de abstracción que:
# 1. Centraliza todas las operaciones de base de datos
# 2. Proporciona una interfaz única para acceder a los datos
# 3. Encapsula la lógica de conexión y manejo de la base de datos
# 4. Permite mantener un código más organizado y mantenible
# 5. Gestiona las conexiones de manera segura
# 6. Maneja los errores y excepciones de la base de datos

class Database:
    """
    Clase que maneja todas las operaciones con la base de datos PostgreSQL.
    Esta clase es la encargada de guardar y recuperar información del sistema.
    """
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO __INIT__
    # =============================================
    # El método __init__ es el constructor de la clase Database.
    # Sus principales funciones son:
    # 1. Recibe los parámetros de conexión a la base de datos
    # 2. Almacena estos parámetros en un diccionario
    # 3. Inicializa la variable de conexión como None
    # 4. Llama al método connect() para establecer la conexión
    # Este método es crucial ya que prepara la clase para su uso
    # y establece la conexión inicial con la base de datos.
    
    def __init__(self, dbname: str, user: str, password: str, host: str, port: str):
        """
        Inicializa la conexión a la base de datos.
        
        Args:
            dbname: Nombre de la base de datos
            user: Usuario de la base de datos
            password: Contraseña del usuario
            host: Dirección del servidor
            port: Puerto de conexión
        """
        self.conn_params = {
            'dbname': dbname,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }
        self.conn = None
        self.connect()
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO CONNECT
    # =============================================
    # El método connect establece la conexión con la base de datos PostgreSQL.
    # Sus principales funciones son:
    # 1. Intenta establecer la conexión usando los parámetros almacenados
    # 2. Configura la conexión para que los cambios se guarden automáticamente
    # 3. Maneja diferentes tipos de errores comunes:
    #    - Base de datos no existe
    #    - Error de autenticación
    #    - Problemas de conexión al servidor
    #    - Otros errores de conexión
    # Este método es esencial para mantener una conexión estable
    # y proporcionar mensajes de error claros al usuario.
    
    def connect(self):
        """
        Establece la conexión con la base de datos.
        Si hay algún error, muestra un mensaje explicativo.
        """
        try:
            self.conn = psycopg2.connect(**self.conn_params)
            self.conn.autocommit = True
        except psycopg2.Error as e:
            error_msg = str(e)
            if "database" in error_msg.lower() and "does not exist" in error_msg.lower():
                raise Exception("La base de datos no existe. Por favor, asegúrese de que la base de datos esté instalada correctamente.")
            elif "password authentication failed" in error_msg.lower():
                raise Exception("Error de autenticación. Verifique las credenciales de la base de datos.")
            elif "could not connect to server" in error_msg.lower():
                raise Exception("No se pudo conectar al servidor de la base de datos. Verifique que el servidor esté en ejecución.")
            else:
                raise Exception(f"Error al conectar a la base de datos: {error_msg}")
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO INSERT_USUARIO
    # =============================================
    # Este método registra un nuevo usuario en el sistema.
    # Funcionalidades principales:
    # 1. Inserta los datos del usuario en la tabla usuarios
    # 2. Asigna automáticamente un ID al nuevo usuario
    # 3. Maneja errores de inserción
    # 4. Retorna True si la operación fue exitosa, False si hubo error

    def insert_usuario(self, usuario: Usuario) -> bool:
        """
        Inserta un nuevo usuario en la base de datos.
        
        Args:
            usuario: Objeto Usuario con los datos a insertar
            
        Returns:
            bool: True si se insertó correctamente, False si hubo error
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO usuarios (nombre, password, nivel, dni, email, telefono, direccion, estado)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id
                """, (
                    usuario.nombre,
                    usuario.password,
                    usuario.nivel,
                    usuario.dni,
                    usuario.email,
                    usuario.telefono,
                    usuario.direccion,
                    usuario.estado
                ))
                usuario.id = cur.fetchone()[0]
                return True
        except psycopg2.Error as e:
            print(f"Error al insertar usuario: {e}")
            return False
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO GET_USUARIO
    # =============================================
    # Este método busca un usuario por su nombre y opcionalmente su contraseña.
    # Funcionalidades principales:
    # 1. Permite búsqueda por nombre solo o nombre y contraseña
    # 2. Retorna un objeto Usuario si encuentra coincidencia
    # 3. Retorna None si no encuentra el usuario
    # 4. Maneja errores de consulta

    def get_usuario(self, nombre: str, password: str = None) -> Optional[Usuario]:
        """
        Obtiene un usuario por su nombre y opcionalmente su contraseña.
        
        Args:
            nombre: Nombre del usuario a buscar
            password: Contraseña del usuario (opcional)
            
        Returns:
            Optional[Usuario]: El usuario encontrado o None si no existe
        """
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                if password:
                    cur.execute("""
                        SELECT * FROM usuarios
                        WHERE nombre = %s AND password = %s
                    """, (nombre, password))
                else:
                    cur.execute("""
                        SELECT * FROM usuarios
                        WHERE nombre = %s
                    """, (nombre,))
                
                row = cur.fetchone()
                if row:
                    return Usuario(
                        id=row['id'],
                        nombre=row['nombre'],
                        password=row['password'],
                        nivel=row['nivel'],
                        dni=row['dni'],
                        email=row['email'],
                        telefono=row['telefono'],
                        direccion=row['direccion'],
                        fecha_registro=row['fecha_registro'],
                        estado=row['estado']
                    )
                return None
        except psycopg2.Error as e:
            print(f"Error al obtener usuario: {e}")
            return None
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO GET_USUARIOS
    # =============================================
    # Este método obtiene la lista completa de usuarios registrados.
    # Funcionalidades principales:
    # 1. Retorna todos los usuarios ordenados por nombre
    # 2. Convierte cada registro en un objeto Usuario
    # 3. Maneja errores de consulta
    # 4. Retorna lista vacía en caso de error

    def get_usuarios(self) -> List[Usuario]:
        """Obtiene todos los usuarios registrados"""
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT * FROM usuarios ORDER BY nombre")
                return [
                    Usuario(
                        id=row['id'],
                        nombre=row['nombre'],
                        password=row['password'],
                        nivel=row['nivel'],
                        dni=row['dni'],
                        email=row['email'],
                        telefono=row['telefono'],
                        direccion=row['direccion'],
                        fecha_registro=row['fecha_registro'],
                        estado=row['estado']
                    )
                    for row in cur.fetchall()
                ]
        except psycopg2.Error as e:
            print(f"Error al obtener usuarios: {e}")
            return []
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO ACTUALIZAR_USUARIO
    # =============================================
    # Este método modifica los datos de un usuario existente.
    # Funcionalidades principales:
    # 1. Actualiza todos los campos modificables del usuario
    # 2. Verifica que el usuario exista antes de actualizar
    # 3. Retorna True si la actualización fue exitosa
    # 4. Maneja errores de actualización

    def actualizar_usuario(self, usuario: Usuario) -> bool:
        """Actualiza los datos de un usuario existente"""
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    UPDATE usuarios
                    SET email = %s,
                        telefono = %s,
                        direccion = %s,
                        password = %s,
                        nivel = %s,
                        estado = %s
                    WHERE id = %s
                """, (
                    usuario.email,
                    usuario.telefono,
                    usuario.direccion,
                    usuario.password,
                    usuario.nivel,
                    usuario.estado,
                    usuario.id
                ))
                return cur.rowcount > 0
        except psycopg2.Error as e:
            print(f"Error al actualizar usuario: {e}")
            return False
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO ELIMINAR_USUARIO
    # =============================================
    # Este método elimina un usuario del sistema.
    # Funcionalidades principales:
    # 1. Elimina el usuario por su ID
    # 2. Verifica que el usuario exista antes de eliminar
    # 3. Retorna True si la eliminación fue exitosa
    # 4. Maneja errores de eliminación

    def eliminar_usuario(self, usuario_id: int) -> bool:
        """Elimina un usuario de la base de datos"""
        try:
            with self.conn.cursor() as cur:
                cur.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
                return cur.rowcount > 0
        except psycopg2.Error as e:
            print(f"Error al eliminar usuario: {e}")
            return False
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO INSERT_LIBRO
    # =============================================
    # Este método registra un nuevo libro en el sistema.
    # Funcionalidades principales:
    # 1. Inserta los datos del libro en la tabla libros
    # 2. Asigna automáticamente un ID al nuevo libro
    # 3. Retorna una tupla (éxito, mensaje_error)
    # 4. Maneja errores de inserción

    def insert_libro(self, libro: Libro) -> tuple:
        """Inserta un nuevo libro en la base de datos. Retorna (success, error_message)"""
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO libros (titulo, autor, isbn, codigo_cdj, categoria_id, editorial, anio_publicacion, estado, cantidad)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id
                """, (
                    libro.titulo,
                    libro.autor,
                    libro.isbn,
                    libro.codigo_cdj,
                    libro.categoria_id,
                    libro.editorial,
                    libro.anio_publicacion,
                    libro.estado,
                    libro.cantidad
                ))
                libro.id = cur.fetchone()[0]
                return True, None
        except psycopg2.Error as e:
            return False, str(e)
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO ACTUALIZAR_LIBRO
    # =============================================
    # Este método modifica los datos de un libro existente.
    # Funcionalidades principales:
    # 1. Actualiza todos los campos modificables del libro
    # 2. Verifica que el libro exista antes de actualizar
    # 3. Retorna True si la actualización fue exitosa
    # 4. Maneja errores de actualización

    def actualizar_libro(self, libro: Libro) -> bool:
        """Actualiza los datos de un libro existente"""
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    UPDATE libros
                    SET titulo = %s,
                        autor = %s,
                        isbn = %s,
                        editorial = %s,
                        anio_publicacion = %s,
                        cantidad = %s,
                        codigo_cdj = %s
                    WHERE id = %s
                """,
                (
                    libro.titulo,
                    libro.autor,
                    libro.isbn,
                    libro.editorial,
                    libro.anio_publicacion,
                    libro.cantidad,
                    libro.codigo_cdj,
                    libro.id
                ))
                return cur.rowcount > 0
        except psycopg2.Error as e:
            print(f"Error al actualizar libro: {e}")
            return False
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO ELIMINAR_LIBRO
    # =============================================
    # Este método elimina un libro del sistema.
    # Funcionalidades principales:
    # 1. Elimina el libro por su ID
    # 2. Verifica que el libro exista antes de eliminar
    # 3. Retorna True si la eliminación fue exitosa
    # 4. Maneja errores de eliminación

    def eliminar_libro(self, libro_id: int) -> bool:
        """Elimina un libro de la base de datos"""
        try:
            with self.conn.cursor() as cur:
                cur.execute("DELETE FROM libros WHERE id = %s", (libro_id,))
                return cur.rowcount > 0
        except psycopg2.Error as e:
            print(f"Error al eliminar libro: {e}")
            return False
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO BUSCAR_LIBROS
    # =============================================
    # Este método busca libros por diferentes criterios.
    # Funcionalidades principales:
    # 1. Busca por título, autor o código CDJ
    # 2. Realiza búsqueda case-insensitive
    # 3. Retorna lista de libros que coinciden
    # 4. Maneja errores de búsqueda

    def buscar_libros(self, termino: str) -> List[Libro]:
        """Busca libros por título, autor o código CDJ"""
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("""
                    SELECT * FROM libros
                    WHERE LOWER(titulo) LIKE %s OR LOWER(autor) LIKE %s OR LOWER(codigo_cdj) LIKE %s
                """, (f"%{termino}%", f"%{termino}%", f"%{termino}%"))
                return [Libro(**dict(row)) for row in cur.fetchall()]
        except psycopg2.Error as e:
            print(f"Error al buscar libros: {e}")
            return []
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO GET_LIBROS
    # =============================================
    # Este método obtiene la lista completa de libros.
    # Funcionalidades principales:
    # 1. Retorna todos los libros ordenados por título
    # 2. Convierte cada registro en un objeto Libro
    # 3. Maneja errores de consulta
    # 4. Retorna lista vacía en caso de error

    def get_libros(self) -> List[Libro]:
        """Obtiene todos los libros registrados"""
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT * FROM libros ORDER BY titulo")
                return [Libro(**dict(row)) for row in cur.fetchall()]
        except psycopg2.Error as e:
            print(f"Error al obtener libros: {e}")
            return []
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO INSERT_PRESTAMO
    # =============================================
    # Este método registra un nuevo préstamo.
    # Funcionalidades principales:
    # 1. Inserta los datos del préstamo en la tabla prestamos
    # 2. Asigna automáticamente un ID al nuevo préstamo
    # 3. Retorna el ID del préstamo creado
    # 4. Maneja errores de inserción

    def insert_prestamo(self, prestamo: Prestamo) -> int:
        """Inserta un nuevo préstamo y retorna su ID."""
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO prestamos (usuario_id, libro_id, fecha_prestamo, 
                                     fecha_devolucion, estado)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
            """, (prestamo.usuario_id, prestamo.libro_id, prestamo.fecha_prestamo,
                  prestamo.fecha_devolucion, prestamo.estado))
            return cur.fetchone()[0]
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO GET_PRESTAMOS_USUARIO
    # =============================================
    # Este método obtiene los préstamos de un usuario específico.
    # Funcionalidades principales:
    # 1. Busca todos los préstamos del usuario
    # 2. Ordena por fecha de préstamo descendente
    # 3. Convierte cada registro en un objeto Prestamo
    # 4. Maneja errores de consulta

    def get_prestamos_usuario(self, usuario_id: int) -> List[Prestamo]:
        """Obtiene todos los préstamos de un usuario."""
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("""
                SELECT * FROM prestamos
                WHERE usuario_id = %s
                ORDER BY fecha_prestamo DESC
            """, (usuario_id,))
            return [Prestamo(**dict(row)) for row in cur.fetchall()]
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO GET_PRESTAMOS_VENCIDOS
    # =============================================
    # Este método obtiene los préstamos que han vencido.
    # Funcionalidades principales:
    # 1. Busca préstamos activos con fecha de devolución pasada
    # 2. Convierte cada registro en un objeto Prestamo
    # 3. Maneja errores de consulta
    # 4. Retorna lista vacía en caso de error

    def get_prestamos_vencidos(self) -> List[Prestamo]:
        """Obtiene todos los préstamos vencidos."""
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("""
                    SELECT * FROM prestamos
                    WHERE estado = 'activo' AND fecha_devolucion < NOW()
                """)
                return [Prestamo(**dict(row)) for row in cur.fetchall()]
        except psycopg2.Error as e:
            print(f"Error al obtener préstamos vencidos: {e}")
            return []
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO ACTUALIZAR_ESTADO_PRESTAMO
    # =============================================
    # Este método actualiza el estado de un préstamo.
    # Funcionalidades principales:
    # 1. Actualiza el estado del préstamo
    # 2. Si el estado es 'devuelto', registra la fecha real
    # 3. Retorna True si la actualización fue exitosa
    # 4. Maneja errores de actualización

    def actualizar_estado_prestamo(self, prestamo_id: int, nuevo_estado: str) -> bool:
        """Actualiza el estado de un préstamo. Si el estado es 'devuelto', también registra la fecha de devolución real."""
        try:
            with self.conn.cursor() as cur:
                if nuevo_estado == "devuelto":
                    from datetime import datetime
                    cur.execute("""
                        UPDATE prestamos
                        SET estado = %s, fecha_devolucion_real = %s
                        WHERE id = %s
                    """, (nuevo_estado, datetime.now(), prestamo_id))
                else:
                    cur.execute("""
                        UPDATE prestamos
                        SET estado = %s
                        WHERE id = %s
                    """, (nuevo_estado, prestamo_id))
                return cur.rowcount > 0
        except psycopg2.Error as e:
            print(f"Error al actualizar estado del préstamo: {e}")
            return False
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO ACTUALIZAR_ESTADO_LIBRO
    # =============================================
    # Este método actualiza el estado de un libro.
    # Funcionalidades principales:
    # 1. Actualiza el estado del libro
    # 2. Verifica que el libro exista
    # 3. Retorna True si la actualización fue exitosa
    # 4. Maneja errores de actualización

    def actualizar_estado_libro(self, libro_id: int, nuevo_estado: str) -> bool:
        """Actualiza el estado de un libro."""
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    UPDATE libros
                    SET estado = %s
                    WHERE id = %s
                """, (nuevo_estado, libro_id))
                return cur.rowcount > 0
        except psycopg2.Error as e:
            print(f"Error al actualizar estado del libro: {e}")
            return False
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO CLOSE
    # =============================================
    # Este método cierra la conexión a la base de datos.
    # Funcionalidades principales:
    # 1. Verifica si existe una conexión activa
    # 2. Cierra la conexión de manera segura
    # 3. Libera los recursos utilizados
    # 4. Es importante llamarlo al finalizar el uso de la base de datos

    def close(self):
        """Cierra la conexión a la base de datos"""
        if self.conn:
            self.conn.close()
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO GET_LIBRO
    # =============================================
    # Este método busca un libro por su código CDJ.
    # Funcionalidades principales:
    # 1. Busca un libro específico por su código CDJ
    # 2. Retorna un objeto Libro si lo encuentra
    # 3. Retorna None si no encuentra el libro
    # 4. Maneja errores de consulta

    def get_libro(self, codigo_cdj: str) -> Optional[Libro]:
        """Obtiene un libro por su código CDJ."""
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("""
                    SELECT * FROM libros
                    WHERE codigo_cdj = %s
                """, (codigo_cdj,))
                row = cur.fetchone()
                if row:
                    return Libro(**dict(row))
                return None
        except psycopg2.Error as e:
            print(f"Error al obtener libro: {e}")
            return None
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO BUSCAR_PRESTAMOS_ACTIVOS_POR_LIBRO
    # =============================================
    # Este método busca préstamos activos de un libro específico.
    # Funcionalidades principales:
    # 1. Busca préstamos activos o pendientes
    # 2. Filtra por ID del libro
    # 3. Convierte cada registro en un objeto Prestamo
    # 4. Maneja errores de consulta

    def buscar_prestamos_activos_por_libro(self, libro_id: int) -> List[Prestamo]:
        """Busca préstamos activos o pendientes para un libro específico"""
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("""
                    SELECT * FROM prestamos
                    WHERE libro_id = %s AND estado IN ('activo', 'pendiente')
                """, (libro_id,))
                return [Prestamo(**dict(row)) for row in cur.fetchall()]
        except psycopg2.Error as e:
            print(f"Error al buscar préstamos activos por libro: {e}")
            return []
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO GET_PRESTAMOS_ACTIVOS
    # =============================================
    # Este método obtiene todos los préstamos activos.
    # Funcionalidades principales:
    # 1. Busca préstamos con estado 'activo'
    # 2. Ordena por fecha de préstamo descendente
    # 3. Convierte cada registro en un objeto Prestamo
    # 4. Maneja errores de consulta

    def get_prestamos_activos(self) -> List[Prestamo]:
        """Obtiene todos los préstamos activos"""
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("""
                    SELECT * FROM prestamos 
                    WHERE estado = 'activo' 
                    ORDER BY fecha_prestamo DESC
                """)
                return [Prestamo(**dict(row)) for row in cur.fetchall()]
        except psycopg2.Error as e:
            print(f"Error al obtener préstamos activos: {e}")
            return []
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO GET_USUARIO_POR_ID
    # =============================================
    # Este método busca un usuario por su ID.
    # Funcionalidades principales:
    # 1. Busca un usuario específico por su ID
    # 2. Retorna un objeto Usuario si lo encuentra
    # 3. Retorna None si no encuentra el usuario
    # 4. Maneja errores de consulta

    def get_usuario_por_id(self, usuario_id: int) -> Optional[Usuario]:
        """Obtiene un usuario por su ID"""
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
                row = cur.fetchone()
                if row:
                    return Usuario(
                        id=row['id'],
                        nombre=row['nombre'],
                        password=row['password'],
                        nivel=row['nivel'],
                        dni=row['dni'],
                        email=row['email'],
                        telefono=row['telefono'],
                        direccion=row['direccion'],
                        fecha_registro=row['fecha_registro']
                    )
                return None
        except psycopg2.Error as e:
            print(f"Error al obtener usuario por ID: {e}")
            return None
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO GET_LIBRO_POR_ID
    # =============================================
    # Este método busca un libro por su ID.
    # Funcionalidades principales:
    # 1. Busca un libro específico por su ID
    # 2. Retorna un objeto Libro si lo encuentra
    # 3. Retorna None si no encuentra el libro
    # 4. Maneja errores de consulta

    def get_libro_por_id(self, libro_id: int) -> Optional[Libro]:
        """Obtiene un libro por su ID"""
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT * FROM libros WHERE id = %s", (libro_id,))
                row = cur.fetchone()
                if row:
                    return Libro(**dict(row))
                return None
        except psycopg2.Error as e:
            print(f"Error al obtener libro por ID: {e}")
            return None
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO GET_PRESTAMOS_PENDIENTES
    # =============================================
    # Este método obtiene los préstamos pendientes de aprobación.
    # Funcionalidades principales:
    # 1. Busca préstamos con estado 'pendiente'
    # 2. Ordena por fecha de préstamo ascendente
    # 3. Convierte cada registro en un objeto Prestamo
    # 4. Maneja errores de consulta

    def get_prestamos_pendientes(self) -> List[Prestamo]:
        """
        Obtiene todos los préstamos que están pendientes de aprobación.
        
        Returns:
            List[Prestamo]: Lista de préstamos pendientes
        """
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("""
                    SELECT * FROM prestamos 
                    WHERE estado = 'pendiente'
                    ORDER BY fecha_prestamo ASC
                """)
                return [Prestamo(**dict(row)) for row in cur.fetchall()]
        except psycopg2.Error as e:
            print(f"Error al obtener préstamos pendientes: {e}")
            return []
    
    # =============================================
    # EXPLICACIÓN DEL MÉTODO GET_CATEGORIAS
    # =============================================
    # Este método obtiene todas las categorías registradas.
    # Funcionalidades principales:
    # 1. Retorna todas las categorías ordenadas por nombre
    # 2. Convierte cada registro en un objeto Categoria
    # 3. Maneja errores de consulta
    # 4. Retorna lista vacía en caso de error

    def get_categorias(self) -> List[Categoria]:
        """
        Obtiene todas las categorías registradas en la base de datos.
        
        Returns:
            List[Categoria]: Lista de todas las categorías
        """
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT * FROM categorias ORDER BY nombre")
                return [Categoria(**dict(row)) for row in cur.fetchall()]
        except Exception as e:
            print(f"Error al obtener categorías: {e}")
            return []

    # =============================================
    # EXPLICACIÓN DEL MÉTODO INSERT_CATEGORIA
    # =============================================
    # Este método registra una nueva categoría.
    # Funcionalidades principales:
    # 1. Inserta los datos de la categoría
    # 2. Asigna automáticamente un ID
    # 3. Retorna True si la inserción fue exitosa
    # 4. Maneja errores de inserción

    def insert_categoria(self, categoria: Categoria) -> bool:
        """
        Inserta una nueva categoría en la base de datos.
        
        Args:
            categoria: Objeto Categoria con los datos a insertar
            
        Returns:
            bool: True si se insertó correctamente, False si hubo error
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO categorias (nombre, descripcion, codigo_cdj)
                    VALUES (%s, %s, %s)
                    RETURNING id
                    """,
                    (categoria.nombre, categoria.descripcion, categoria.codigo_cdj)
                )
                categoria.id = cur.fetchone()[0]
                return True
        except Exception as e:
            print(f"Error al insertar categoría: {e}")
            return False

    # =============================================
    # EXPLICACIÓN DEL MÉTODO ACTUALIZAR_CATEGORIA
    # =============================================
    # Este método modifica una categoría existente.
    # Funcionalidades principales:
    # 1. Actualiza los datos de la categoría
    # 2. Verifica que la categoría exista
    # 3. Retorna True si la actualización fue exitosa
    # 4. Maneja errores de actualización

    def actualizar_categoria(self, categoria: Categoria) -> bool:
        """Actualiza los datos de una categoría existente"""
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE categorias
                    SET nombre = %s, descripcion = %s, codigo_cdj = %s
                    WHERE id = %s
                    """,
                    (categoria.nombre, categoria.descripcion, categoria.codigo_cdj, categoria.id)
                )
                return cur.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar categoría: {e}")
            return False

    # =============================================
    # EXPLICACIÓN DEL MÉTODO ELIMINAR_CATEGORIA
    # =============================================
    # Este método elimina una categoría.
    # Funcionalidades principales:
    # 1. Elimina la categoría por su ID
    # 2. Verifica que la categoría exista
    # 3. Retorna True si la eliminación fue exitosa
    # 4. Maneja errores de eliminación

    def eliminar_categoria(self, categoria_id: int) -> bool:
        """Elimina una categoría de la base de datos"""
        try:
            with self.conn.cursor() as cur:
                cur.execute("DELETE FROM categorias WHERE id = %s", (categoria_id,))
                return cur.rowcount > 0
        except Exception as e:
            raise

    # =============================================
    # EXPLICACIÓN DEL MÉTODO GET_TODOS_PRESTAMOS
    # =============================================
    # Este método obtiene el histórico completo de préstamos.
    # Funcionalidades principales:
    # 1. Retorna todos los préstamos ordenados por fecha
    # 2. Convierte cada registro en un objeto Prestamo
    # 3. Maneja errores de consulta
    # 4. Retorna lista vacía en caso de error

    def get_todos_prestamos(self):
        """Obtiene todos los préstamos del sistema (histórico completo)"""
        try:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT * FROM prestamos ORDER BY fecha_prestamo DESC")
                return [Prestamo(**dict(row)) for row in cur.fetchall()]
        except psycopg2.Error as e:
            print(f"Error al obtener todos los préstamos: {e}")
            return []

    # =============================================
    # EXPLICACIÓN DEL MÉTODO TIENE_PRESTAMO_ACTIVO
    # =============================================
    # Este método verifica si un usuario tiene un préstamo activo.
    # Funcionalidades principales:
    # 1. Verifica préstamos activos por usuario y libro
    # 2. Retorna True si existe un préstamo activo
    # 3. Retorna False si no hay préstamo activo
    # 4. Maneja errores de consulta

    def tiene_prestamo_activo(self, usuario_id: int, libro_id: int) -> bool:
        """Verifica si un usuario ya tiene un préstamo activo de un libro específico."""
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT COUNT(*) 
                    FROM prestamos 
                    WHERE usuario_id = %s 
                    AND libro_id = %s 
                    AND estado = 'activo'
                """, (usuario_id, libro_id))
                return cur.fetchone()[0] > 0
        except psycopg2.Error as e:
            print(f"Error al verificar préstamo activo: {e}")
            return False 