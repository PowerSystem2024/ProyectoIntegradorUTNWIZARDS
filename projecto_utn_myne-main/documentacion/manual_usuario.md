# Manual de Usuario - Sistema de Gestión de Biblioteca

## Índice
1. [Introducción](#introducción)
2. [Acceso al Sistema](#acceso-al-sistema)
3. [Menú Principal](#menú-principal)
4. [Funcionalidades](#funcionalidades)
5. [Solución de Problemas](#solución-de-problemas)

## Introducción
Este manual está diseñado para guiar a los usuarios en el uso del Sistema de Gestión de Biblioteca. El sistema permite consultar libros, solicitar préstamos, ver el historial de préstamos y gestionar datos personales.

## Acceso al Sistema
1. Inicie el programa
2. Ingrese su nombre de usuario y contraseña
3. Si es su primer acceso, contacte al administrador para obtener sus credenciales
4. **Nota:** Si su usuario está inactivo o la contraseña es incorrecta, no podrá acceder. Contacte al administrador si tiene problemas de acceso.

## Menú Principal
El menú principal ofrece las siguientes opciones:
1. Consultas/Listar Libros
2. Solicitar préstamo
3. Ver mis préstamos
4. Historial
5. Modificar mis datos
6. Salir

## Funcionalidades

### 1. Consultas/Listar Libros
Permite buscar y listar libros de diferentes formas:
- Por autor
- Por categoría (CDJ)
- Navegando por categorías
- Listado general

#### Búsqueda por Autor
1. Seleccione "Listar libros por autor"
2. Ingrese el nombre o parte del nombre del autor
3. Se mostrará una tabla con los libros encontrados

#### Búsqueda por Categoría
1. Seleccione "Listar libros por categoría"
2. Ingrese el código CDJ (dos dígitos) o un dígito para ver todas las categorías que empiecen con ese número
3. Se mostrarán los libros de la categoría seleccionada

### 2. Solicitar Préstamo
Para solicitar un préstamo:
1. Seleccione "Solicitar préstamo"
2. Ingrese el código CDJ del libro
3. Confirme la solicitud
4. La solicitud quedará pendiente de aprobación por un administrador

**Notas importantes:**
- Máximo 5 libros prestados o reservados simultáneamente
- No se pueden solicitar libros si hay préstamos vencidos
- No se puede solicitar el mismo libro dos veces
- El libro debe estar disponible
- Si la solicitud es rechazada, recibirá un mensaje de error
- Si su usuario está inactivo, no podrá solicitar préstamos

### 3. Ver Mis Préstamos
Muestra los préstamos activos actuales:
- Código CDJ del libro
- ISBN
- Título
- Autor
- Cantidad

### 4. Historial
Ofrece diferentes formas de consultar el historial de préstamos:
- Por autor
- Por código CDJ
- Entre fechas
- Libros más solicitados
- Listado completo

#### Historial por Autor
1. Seleccione "Buscar Historial por Autor"
2. Ingrese el nombre del autor
3. Se mostrará una tabla con los préstamos realizados de libros de ese autor

#### Historial entre Fechas
1. Seleccione "Buscar entre fechas"
2. Ingrese la fecha inicial (DD-MM-YYYY)
3. Ingrese la fecha final (DD-MM-YYYY)
4. Se mostrarán los préstamos realizados en ese período
5. **Nota:** Si no hay resultados, se mostrará un mensaje de advertencia.

### 5. Modificar Mis Datos
Permite actualizar información personal:
- Contraseña (mínimo 6 caracteres)
- Email (formato válido)
- Dirección
- **Validaciones:** El email debe ser válido y la contraseña debe tener al menos 6 caracteres.

### 6. Devolución de Libros
- Si devuelve un libro fuera de plazo, el sistema lo notificará.
- Si intenta devolver un libro que no tiene prestado, recibirá un mensaje de error.

## Solución de Problemas

### Problemas Comunes

1. **No puedo iniciar sesión**
   - Verifique su usuario y contraseña
   - Si su usuario está inactivo, contacte al administrador

2. **No puedo solicitar un préstamo**
   - Verifique que no tenga 5 libros prestados o reservados
   - Asegúrese de no tener préstamos vencidos
   - Confirme que el libro esté disponible
   - No puede solicitar el mismo libro dos veces
   - Si la solicitud es rechazada, consulte con el administrador

3. **No encuentro un libro**
   - Verifique el código CDJ
   - Intente buscar por autor
   - Consulte con el administrador

4. **Olvidé mi contraseña**
   - Contacte al administrador para restablecerla

5. **No puedo modificar mis datos**
   - Verifique que el email sea válido
   - La contraseña debe tener al menos 6 caracteres

6. **No aparecen resultados en el historial**
   - Puede que no haya préstamos registrados con esos criterios

### Contacto
Si necesita ayuda adicional, contacte al administrador del sistema. 