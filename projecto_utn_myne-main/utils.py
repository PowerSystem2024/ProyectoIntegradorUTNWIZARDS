# ===== UTILS.PY =====
# Este archivo contiene funciones de utilidad para hacer el sistema más amigable.
# Es como una caja de herramientas que ayuda a:
# 1. Mostrar información de manera bonita (títulos, mensajes, tablas)
# 2. Validar datos (DNI, ISBN, códigos CDJ)
# 3. Manejar fechas y cálculos
# 4. Interactuar con el usuario (menús, confirmaciones)

# ===== IMPORTACIÓN DE LAS HERRAMIENTAS NECESARIAS =====

# Importamos las herramientas necesarias para manejar los datos que usamos en el sistema
# y para interactuar con el usuario.

import os
from datetime import datetime, timedelta
from typing import List, Optional
from colorama import init, Fore, Style
from tabulate import tabulate
from config import (
    DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT,
    MAX_LIBROS_POR_USUARIO, DIAS_PRESTAMO,
    ADMIN_USERNAME, ADMIN_PASSWORD
)

# Inicializamos colorama para que los colores funcionen correctamente en la consola
init()

# ===== FUNCIONES DE UTILIDAD =====

# Función que limpia la pantalla de la consola
def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    # Esta función limpia la pantalla de la consola para mantener la interfaz ordenada
    # En Windows usa 'cls', en otros sistemas usa 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

# Función que muestra un título formateado
def mostrar_titulo(titulo: str):
    """Muestra un título formateado."""
    # Esta función crea un título formateado con marco y colores
    # Útil para separar secciones del programa y mejorar la visualización
    print(f"\n{Fore.CYAN}{Style.BRIGHT}{'=' * 50}")
    print(f"{titulo.center(50)}")
    print(f"{'=' * 50}{Style.RESET_ALL}\n")

# Función que muestra un mensaje de error en rojo
def mostrar_error(mensaje: str):
    """Muestra un mensaje de error en rojo."""
    # Esta función muestra mensajes de error en rojo con ícono
    # Ayuda al usuario a identificar cuando algo salió mal
    print(f"\n{Fore.RED}❌ {mensaje}{Style.RESET_ALL}")

# Función que muestra un mensaje de éxito en verde
def mostrar_exito(mensaje: str):
    """Muestra un mensaje de éxito en verde."""
    # Esta función muestra mensajes de éxito en verde con ícono
    # Confirma al usuario que una acción se completó correctamente
    print(f"\n{Fore.GREEN}✅ {mensaje}{Style.RESET_ALL}")

# Función que muestra un mensaje de advertencia en amarillo
def mostrar_advertencia(mensaje: str):
    """Muestra un mensaje de advertencia en amarillo."""
    # Esta función muestra advertencias en amarillo con ícono
    # Alerta al usuario sobre información importante
    print(f"\n{Fore.YELLOW}⚠️ {mensaje}{Style.RESET_ALL}")

# Función que formatea una fecha en formato dd-mm-yyyy
def formatear_fecha(fecha: datetime) -> str:
    """Formatea una fecha en formato dd-mm-yyyy."""
    # Esta función convierte fechas a formato legible
    # Transforma fechas a formato dd-mm-yyyy para mejor visualización
    return fecha.strftime("%d-%m-%Y")

# Función que calcula la fecha de devolución basada en la configuración
def calcular_fecha_devolucion() -> datetime:
    """Calcula la fecha de devolución basada en la configuración."""
    # Esta función calcula la fecha de devolución de un libro
    # Suma los días de préstamo configurados a la fecha actual
    return datetime.now() + timedelta(days=DIAS_PRESTAMO)

# Función que valida el formato del DNI
def validar_dni(dni: str) -> bool:
    """Valida el formato del DNI."""
    # Esta función verifica que el DNI sea válido
    # Comprueba que tenga exactamente 8 números
    return dni.isdigit() and len(dni) == 8

# Función que valida el formato del ISBN
def validar_isbn(isbn: str) -> bool:
    """Valida el formato del ISBN."""
    # Eliminar guiones y espacios
    isbn = isbn.replace('-', '').replace(' ', '')
    # Esta función verifica que el ISBN sea válido
    # Comprueba que tenga 10 o 13 números (sin guiones)
    return isbn.isdigit() and len(isbn) in [10, 13]

# Función que valida el formato del código CDJ
def validar_cdj(cdj: str) -> bool:
    """Valida el formato del código CDJ."""
    # El código CDJ debe tener el formato: XXX.XX
    partes = cdj.split('.')
    # Esta función verifica que el código CDJ sea válido
    # Comprueba que tenga el formato correcto (XXX.XX)
    return len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit()

# Función que muestra una tabla formateada
def mostrar_tabla(encabezados: list, datos: list):
    """Muestra una tabla formateada."""
    # Esta función muestra datos en formato de tabla
    # Organiza la información de manera clara y ordenada
    print(tabulate(datos, headers=encabezados, tablefmt="grid"))

# Función que espera a que el usuario presione una tecla
def esperar_tecla():
    """Espera a que el usuario presione una tecla."""
    # Esta función pausa la pantalla esperando Enter
    # Permite al usuario leer la información antes de continuar
    input("\nPresione Enter para continuar...")

# Función que pide confirmación al usuario para una acción
def confirmar_accion(mensaje: str) -> bool:
    """Pide confirmación al usuario para una acción."""
    # Esta función pide confirmación al usuario
    # Útil para acciones importantes que requieren confirmación
    respuesta = input(f"\n{mensaje} (s/n): ").lower()
    return respuesta == 's'

# Función que muestra un menú y retorna la opción seleccionada
def mostrar_menu(opciones: list) -> str:
    """Muestra un menú y retorna la opción seleccionada."""
    # Esta función muestra un menú numerado y valida la selección
    # Permite al usuario elegir opciones de manera segura
    for opcion in opciones:
        print(opcion)
    # Mientras el usuario no seleccione una opción válida, se muestra un mensaje de error
    while True:
        seleccion = input("\nSeleccione una opción: ").strip()
        if seleccion in [str(i) for i in range(1, len(opciones) + 1)]:
            return seleccion
        mostrar_error("Opción inválida")

def limpiar_texto(texto):
    if not texto:
        return texto
    # Reemplaza caracteres no válidos por un espacio o los elimina
    return ''.join(c for c in texto if c.isprintable() and ord(c) < 128) 