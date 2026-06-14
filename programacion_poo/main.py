# Programa principal usando Programación Orientada a Objetos.

from mascota import Mascota


def main():
    """Crea objetos de la clase Mascota y ejecuta sus métodos."""

    mascota1 = Mascota("Firulais", "Perro", 5)
    mascota2 = Mascota("Michi", "Gato", 3)

    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()

    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()


if __name__ == "__main__":
    main()