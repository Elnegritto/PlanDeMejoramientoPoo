# Inicialmente hacemos la definición de la clase que va a ser la base, Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        print(f"{self.marca} {self.modelo}")

# En esta parte la se hace la definición de una clase por asi decirlo derivada llamada Carro que hereda de la clase llamada Vehiculo
class Carro(Vehiculo):
    def __init__(self, marca, modelo, color):
        # Por aqui se Llama al constructor de la clase base usando super()
        super().__init__(marca, modelo)
        # Aqui añadimos un nuevo atributo de instancia
        self.color = color

    # Este es método adicional en la clase derivada
    def infoCarro(self):
        print(f"{self.marca} {self.modelo} (Color {self.color})")

# Ya casi finalizando hacemos una instancia de la clase Carro
coche1 = Carro("Toyota", "Land Cruiser", "Azul")

# Por se accede a los atributos y se llama a los métodos
coche1.info()        # Este es el método de la clase base osea la clase llamada Vehiculo
coche1.infoCarro()  # Este es el método de la clase derivada el cual la llamada carro
