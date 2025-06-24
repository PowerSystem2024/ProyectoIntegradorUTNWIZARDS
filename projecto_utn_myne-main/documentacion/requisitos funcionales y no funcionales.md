# Requisitos del Sistema de Gestión de Biblioteca

## Requisitos Funcionales

### Gestión de Usuarios
1. El sistema debe permitir el registro de usuarios con roles diferenciados (administrador y usuario normal).
2. Los usuarios deben poder iniciar sesión con nombre de usuario y contraseña.
3. El sistema debe validar que el DNI y nombre de usuario sean únicos y que el email tenga formato válido.
4. Los administradores deben poder gestionar (crear, modificar, eliminar, activar/inactivar, listar) usuarios.
5. Solo el usuario principal "admin" puede eliminar otros administradores.
6. No se puede eliminar un usuario con préstamos activos o pendientes.
7. El nivel de usuario debe ser válido (usuario/admin).

### Gestión de Libros
1. El sistema debe permitir el registro de libros con información detallada (título, autor, ISBN, CDJ, etc.).
2. Cada libro debe tener un código CDJ único y válido según su categoría.
3. El sistema debe validar que el ISBN sea único y que la categoría exista.
4. Los administradores deben poder gestionar (crear, modificar, eliminar, buscar, listar) libros.
5. El sistema debe mantener un registro de la cantidad de ejemplares disponibles y no permitir reducirla por debajo de los préstamos activos.
6. No se puede asignar un CDJ o ISBN ya existente a otro libro.

### Gestión de Categorías
1. El sistema debe permitir la creación y gestión de categorías de libros.
2. Cada categoría debe tener un código CDJ único.
3. Al modificar el CDJ de una categoría, se deben actualizar los CDJ de los libros asociados.
4. No se debe permitir eliminar categorías que tengan libros asignados.

### Gestión de Préstamos
1. Los usuarios normales solo pueden solicitar préstamos (estado "pendiente").
2. Los administradores pueden prestar directamente (estado "activo") y aprobar/rechazar solicitudes.
3. El sistema debe validar que:
   - Un usuario no pueda solicitar el mismo libro dos veces
   - Un usuario no supere el máximo de préstamos permitidos
   - Un usuario no pueda solicitar si tiene préstamos vencidos
   - El usuario debe estar activo
   - No se puede aprobar una solicitud ya procesada
   - No se puede aprobar si no hay ejemplares disponibles
4. El sistema debe registrar la fecha real de devolución.

### Reportes y Consultas
1. El sistema debe permitir consultar:
   - Libros disponibles
   - Préstamos activos
   - Préstamos vencidos
   - Historial de préstamos por usuario
2. Los administradores deben poder exportar reportes a CSV.
3. El sistema debe manejar errores de exportación y notificar al usuario.

## Requisitos No Funcionales

### Seguridad
1. Las contraseñas deben tener un mínimo de 6 caracteres.
2. Los datos sensibles deben estar protegidos en la base de datos.
3. Solo los administradores pueden realizar operaciones críticas.

### Usabilidad
1. La interfaz debe ser intuitiva y fácil de usar.
2. Los mensajes de error deben ser claros, descriptivos y reflejar las validaciones del sistema.
3. El sistema debe permitir salir de cualquier operación escribiendo "salir".

### Rendimiento
1. El sistema debe manejar eficientemente múltiples usuarios.
2. Las consultas a la base de datos deben ser optimizadas.
3. La respuesta del sistema debe ser rápida (< 2 segundos).

### Mantenibilidad
1. El código debe estar bien documentado.
2. La estructura del sistema debe permitir fácilmente agregar nuevas funcionalidades.
3. El sistema debe ser fácil de mantener y actualizar.

### Confiabilidad
1. El sistema debe mantener la integridad de los datos.
2. Debe haber validaciones para prevenir inconsistencias.
3. El sistema debe manejar adecuadamente los errores y excepciones.

### Compatibilidad
1. El sistema debe funcionar en sistemas operativos Windows.
2. Debe ser compatible con PostgreSQL.
3. Debe funcionar con Python 3.x.

### Escalabilidad
1. El sistema debe poder manejar un crecimiento en la cantidad de:
   - Usuarios
   - Libros
   - Préstamos
2. La estructura de la base de datos debe permitir futuras expansiones. 