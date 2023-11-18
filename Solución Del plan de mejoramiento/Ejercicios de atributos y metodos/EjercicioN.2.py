# Bueno inicialmente hacemos la definición de la clase Libro
class Libro:
    # Por aqui se hace el atributo de la clase
    tipoDeMaterial = "Papel"

    # Aqui utilizamos un método de inicialización
    def __init__(self, titulo, autor, paginas):
        # Estos son los atributos de la instancia
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Por aqui vemos el método de la instancia
    def infoLibro(self):
        print(f"Libro: {self.titulo} - Autor: {self.autor} - Páginas: {self.paginas}")

# Aqui Creamos una instancia de la clase Libro
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 100)

# Y finalmente accedemos a los atributos y llamamos a los métodos
print(f"El tipo de material del libro es: {Libro.tipoDeMaterial}")
libro1.infoLibro()
