# Iniciamos nuevamente con definición de una clase llamada Deporte
class Deporte:
    def jugar(self):
        pass

# Por aqui hacemos la definición de la clase llamada como Futbol que hereda de la clase Deporte
class Futbol(Deporte):
    def jugar(self):
        return "¡Gol!"

# Por aqui hacemos nuevamente una definición de la clase llamada como Baloncesto que hereda de la clase Deporte
class Baloncesto(Deporte):
    def jugar(self):
        return "¡Canasta!"

# Ya aqui en esta parte hacemos una función que muestra la acción de puntuacion en cualquier deporte
def realizacionDePuntuacion(deporte):
    return deporte.jugar()

# Ya casi,casi,casi finalizando creamos instancias de las clases derivadas
futbol = Futbol()
baloncesto = Baloncesto()

# Ya por ultimo muestro como se grita cada punto en el respectivo deporte usando polimorfismo
print(f"En el fútbol se grita un punto como: {realizacionDePuntuacion(futbol)}")
print(f"En el baloncesto se grita un punto como: {realizacionDePuntuacion(baloncesto)}")
