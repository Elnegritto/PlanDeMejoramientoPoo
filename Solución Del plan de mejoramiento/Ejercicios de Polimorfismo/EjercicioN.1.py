# Aqui se hace definición de la clase Figura
class Figura:
    def area(self):
        pass

# Por esta parte se hace la definición de la clase Circulo que hereda de Figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio**2

# Por aqui se hace la definición de la clase Cuadrado que hereda de Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado**2

# Esta es la función que calcula el área de cualquier figura
def calcular_area(figura):
    return figura.area()

# En esta parte se crea instancias de las clases
circulo = Circulo(5)
cuadrado = Cuadrado(4)

# Y finalmente se Calcula y muestra las áreas usando polimorfismo
print(f"Área del círculo es: {calcular_area(circulo)}")
print(f"Área del cuadrado es: {calcular_area(cuadrado)}")

