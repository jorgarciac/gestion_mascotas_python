# Clase Mascota que representa una mascota con sus atributos y métodos.

class Mascota:
    """Representa una mascota con nombre, especie y edad."""

    def __init__(self, nombre, especie, edad):
        """Inicializa los atributos de la mascota."""
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """Muestra la información básica de la mascota."""
        print("\n--- Información de la mascota ---")
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")

    def hacer_sonido(self):
        """Muestra un sonido referencial según la especie."""
        if self.especie.lower() == "perro":
            print(f"{self.nombre} dice: ¡Guau!")
        elif self.especie.lower() == "gato":
            print(f"{self.nombre} dice: ¡Miau!")
        else:
            print(f"{self.nombre} hace un sonido característico de su especie.")