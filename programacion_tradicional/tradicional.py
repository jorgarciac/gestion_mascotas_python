# Programa tradicional para registrar y mostrar información de una mascota
# No se utilizan clases ni objetos, solo variables y funciones.

def registrar_mascota():
    """Solicita por teclado los datos básicos de una mascota."""
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")

    return nombre, especie, edad


def mostrar_informacion(nombre, especie, edad):
    """Muestra la información registrada de la mascota."""
    print("\n--- Información de la mascota ---")
    print(f"Nombre: {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad: {edad} años")


def main():
    """Función principal del programa."""
    nombre, especie, edad = registrar_mascota()
    mostrar_informacion(nombre, especie, edad)


if __name__ == "__main__":
    main()