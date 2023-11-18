# Iniciando hacemos la definición de la clase la cual va a ser la base y la llame animal 
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        pass

# Aqui hacemos la definición de la clase derivada la cual llame como Perro la cual va heredar de la clase animal
class Perro(Animal):
    def sonido(self):
        return "Guau"

# Aqui hacemos otra definición pero esta con una nueva clase derivada llamada gato la cual hereda de la clase llamada animal 
class Gato(Animal):
    def sonido(self):
        return "Miau"

# Por aqui Creamos las instancias de las clases derivadas
perro1 = Perro("Princesa")
gato1 = Gato("Panda")

# Y finalmente accedemos a los atributos y llamamos a los métodos
print(f"{perro1.nombre} hace: {perro1.sonido()}")
print(f"{gato1.nombre} hace: {gato1.sonido()}")
