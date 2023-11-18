# Iniciamos con la definición de la clase Pelota
class Pelota:
    # Este es un atributo de la clase
    material = "Goma"

    # Por aqui vemos el método de inicialización
    def __init__(self, color, diametro):
        # Los atributos de esta instancia
        self.color = color
        self.diametro = diametro

    # Método de dicha instancia 
    def infoPelota(self):
        print(f"Detalles de la Pelota: Color - {self.color}, Diámetro - {self.diametro} cm")

# Por aqui creamos una instancia de la clase Pelota
pelota1 = Pelota("Roja con rayas Celestes", 15)

# Y finalmente accedemos a los atributos y a llamar los métodos
print(f"Material de la pelota es: {Pelota.material}")
pelota1.infoPelota()
