# Iniciamos con una Definición de la clase llamada Fruta
class Fruta:
    def sabor(self):
        pass

# En esta parte hacemos la definición de la clase llamada Mandarina que hereda de la clase llamada Fruta
class Mandarina(Fruta):
    def sabor(self):
        return "Dulce"

# Aqui hacemos una nueva definición ahora con una clase llamada Limón que hereda de la clase Fruta
class Limon(Fruta):
    def sabor(self):
        return "Ácido"

# Por aqui hacemos una función que devuelve el sabor de cualquier fruta
def obtenerSabor(fruta):
    return fruta.sabor()

# Ya casi finalizando Creamos las instancias de las clases derivadas
mandarina = Mandarina()
limon = Limon()

# Finalizando ya con esta vaina Obtenemos y mostramos los sabores usando polimorfismo
print(f"La mandarina tiene un sabor: {obtenerSabor(mandarina)}")
print(f"El limón tiene un sabor: {obtenerSabor(limon)}")
