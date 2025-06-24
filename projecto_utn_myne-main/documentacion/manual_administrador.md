# Manual de Administrador - Sistema de Gestión de Biblioteca

## Índice
1. [Introducción](#introducción)
2. [Acceso al Sistema](#acceso-al-sistema)
3. [Menú Principal](#menú-principal)
4. [Gestión de Usuarios](#gestión-de-usuarios)
5. [Gestión de Libros](#gestión-de-libros)
6. [Gestión de Préstamos](#gestión-de-préstamos)
7. [Gestión de Categorías](#gestión-de-categorías)
8. [Reportes](#reportes)
9. [Solución de Problemas](#solución-de-problemas)

## Introducción
Este manual está diseñado para guiar a los administradores en el uso del Sistema de Gestión de Biblioteca. El sistema permite gestionar usuarios, libros, préstamos, categorías y generar reportes.

## Acceso al Sistema
1. Inicie el programa
2. Ingrese las credenciales de administrador
3. El usuario principal "admin" tiene privilegios especiales

## Menú Principal
El menú principal ofrece las siguientes opciones:
1. Gestión de Usuarios
2. Consultas/Listar Libros
3. Gestión de Libros
4. Gestión de Préstamos
5. Gestión de Categorías
6. Reportes
7. Salir

## Gestión de Usuarios

### Registrar Nuevo Usuario
1. Seleccione "Registrar nuevo usuario"
2. Complete los datos requeridos:
   - Nombre de usuario (único)
   - Contraseña (mínimo 6 caracteres)
   - DNI (único, entre 1.000.000 y 99.999.999)
   - Email (opcional)
   - Teléfono (opcional)
   - Dirección (opcional)
   - Nivel (usuario/admin)

### Modificar Usuario
1. Seleccione "Modificar usuario"
2. Ingrese el nombre del usuario
3. Modifique los campos deseados
4. Confirme los cambios

### Eliminar Usuario
1. Seleccione "Eliminar usuario"
2. Ingrese el nombre del usuario
3. Confirme la eliminación
4. Solo el usuario "admin" puede eliminar otros administradores

## Gestión de Libros

### Registrar Nuevo Libro
1. Seleccione "Registrar nuevo libro"
2. Complete los datos:
   - Título
   - Autor
   - ISBN (único)
   - Editorial
   - Año de publicación
   - Cantidad de ejemplares
   - Código CDJ (formato: XXYYY, donde XX es la categoría)

### Modificar Libro
1. Seleccione "Modificar libro"
2. Ingrese el código CDJ
3. Modifique los campos deseados
4. Confirme los cambios

### Eliminar Libro
1. Seleccione "Eliminar libro"
2. Ingrese el código CDJ
3. Confirme la eliminación

## Gestión de Préstamos

### Realizar Préstamo
1. Seleccione "Realizar préstamo"
2. Ingrese el nombre del usuario
3. Ingrese el código CDJ del libro
4. Confirme el préstamo

### Devolver Libro
1. Seleccione "Devolver libro"
2. Ingrese el nombre del usuario
3. Seleccione el libro a devolver
4. Confirme la devolución

### Aprobar Solicitudes
1. Seleccione "Aprobar solicitudes pendientes"
2. Para cada solicitud:
   - Aprobar (a)
   - Rechazar (r)
   - Omitir (Enter)

## Gestión de Categorías

### Agregar Categoría
1. Seleccione "Agregar categoría"
2. Ingrese:
   - Nombre
   - Descripción
   - Código CDJ (00-99)

### Modificar Categoría
1. Seleccione "Modificar categoría"
2. Ingrese el código CDJ
3. Modifique los campos deseados
4. Confirme los cambios

### Eliminar Categoría
1. Seleccione "Eliminar categoría"
2. Ingrese el código CDJ
3. Confirme la eliminación
4. No se puede eliminar si tiene libros asignados

## Reportes

### Tipos de Reportes
1. Libros más prestados
2. Usuarios con más préstamos
3. Libros disponibles
4. Libros no disponibles
5. Libros prestados por usuario
6. Libros atrasados por usuario
7. Libros atrasados en general

### Exportar Reportes
- Todos los reportes pueden exportarse a CSV
- Los archivos se guardan en la carpeta "Descargas Sistema"
- El nombre incluye la fecha y hora de generación

## Solución de Problemas

### Problemas Comunes

1. **Error al eliminar categoría**
   - Verifique que no haya libros asignados
   - Reasigne los libros a otra categoría

2. **Error al modificar CDJ de categoría**
   - Confirme que el nuevo código no esté en uso
   - Verifique que los libros se actualicen correctamente

3. **Error en préstamos**
   - Verifique la disponibilidad del libro
   - Confirme que el usuario no exceda el límite
   - Revise si hay préstamos vencidos

### Mantenimiento del Sistema

1. **Backup de datos**
   - Los archivos CSV se generan en "Descargas Sistema"
   - Realice copias de seguridad periódicas

2. **Actualización de datos**
   - Verifique regularmente los préstamos vencidos
   - Actualice el estado de los libros
   - Revise los reportes de uso

### Contacto
Para soporte técnico o problemas graves, contacte al desarrollador del sistema. 