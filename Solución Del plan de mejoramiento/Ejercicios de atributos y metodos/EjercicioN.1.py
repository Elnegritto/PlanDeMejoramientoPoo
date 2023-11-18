# Para empezar se hace la definición de una clase llamada Persona
class Persona:
    # Este es el atributo de la clase
    especie = "Humano"

    # Aqui se utiliza Método de inicialización, constructor
    def __init__(self, nombre, edad):
        # Estos son los atributos de instancia
        self.nombre = nombre
        self.edad = edad

    # Esto el método de instancia
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Aqui se Crea una instancia de la clase Persona
persona1 = Persona("Kevin", 17)

# Por aqui se accede a los atributos
print(f"Nombre: {persona1.nombre}")
print(f"Edad: {persona1.edad}")

# Y finalmente Llamamos el método
persona1.saludar()
