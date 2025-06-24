-- Script de creación de la estructura de la base de datos para el sistema de gestión de biblioteca
-- Compatible con PostgreSQL 12+

-- Tabla de categorías
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    codigo_cdj VARCHAR(2) NOT NULL UNIQUE
);

-- Tabla de usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    password VARCHAR(128) NOT NULL,
    nivel VARCHAR(10) NOT NULL CHECK (nivel IN ('admin', 'usuario')),
    dni VARCHAR(10) NOT NULL UNIQUE,
    email VARCHAR(100),
    telefono VARCHAR(30),
    direccion VARCHAR(200),
    estado VARCHAR(10) NOT NULL DEFAULT 'activo' CHECK (estado IN ('activo', 'inactivo')),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de libros
CREATE TABLE libros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    codigo_cdj VARCHAR(10) NOT NULL UNIQUE,
    categoria_id INTEGER NOT NULL REFERENCES categorias(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    editorial VARCHAR(100),
    anio_publicacion INTEGER,
    estado VARCHAR(15) NOT NULL DEFAULT 'disponible' CHECK (estado IN ('disponible', 'prestado', 'reservado')),
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de préstamos
CREATE TABLE prestamos (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON UPDATE CASCADE ON DELETE CASCADE,
    libro_id INTEGER NOT NULL REFERENCES libros(id) ON UPDATE CASCADE ON DELETE CASCADE,
    fecha_prestamo TIMESTAMP NOT NULL,
    fecha_devolucion TIMESTAMP NOT NULL,
    fecha_devolucion_real TIMESTAMP,
    estado VARCHAR(15) NOT NULL CHECK (estado IN ('pendiente', 'activo', 'devuelto', 'rechazado'))
);

-- Índices y restricciones adicionales
CREATE INDEX idx_libros_categoria ON libros(categoria_id);
CREATE INDEX idx_prestamos_usuario ON prestamos(usuario_id);
CREATE INDEX idx_prestamos_libro ON prestamos(libro_id);

-- La validación para evitar préstamos activos/pendientes duplicados por usuario y libro se realiza desde la aplicación. 