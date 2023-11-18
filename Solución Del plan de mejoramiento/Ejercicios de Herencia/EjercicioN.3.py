# por aqui iniciamos la definición de la clase base como InstrumentoMusical
class InstrumentoMusical:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar(self):
        pass

# Por aqui hacemos la definición de la clase derivada lllamada Guitarra que hereda obviamente de la clase InstrumentoMusical
class Guitarra(InstrumentoMusical):
    def tocar(self):
        return "Haz sonar la guitarra"

# por aqui hacemos una definición de una clase derivada llamada como Piano que hereda obviamente de InstrumentoMusical
class Piano(InstrumentoMusical):
    def tocar(self):
        return "Haz sonar el piano"

# Por aqui ya finalizando Creamos las instancias de las clases derivadas
guitarra1 = Guitarra("Kevinsho")
piano1 = Piano("Sebastian")

# Y bueno finalizamos accediendo a los atributos y llamando a los métodos
print(f"{guitarra1.nombre}: {guitarra1.tocar()}")
print(f"{piano1.nombre}: {piano1.tocar()}")
