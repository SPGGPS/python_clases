class Producto:
    def __init__ (self, nombre, precio, cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"

    def actualizar_precio(self,nuevo_precio):
        if nuevo_precio > 0:
            self.precio=nuevo_precio

    def actualizar_cantidad(self,nueva_cantidad):
        if nueva_cantidad > 0:
            self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.canitad

class Inventario (Producto):
    def __init__ (self):
        super().__init__(nombre, precio, cantidad)
        self.inventario = []

    def agregar_producto(self,producto):
        self.inventario.append([super.nombre,super.precio,super.cantidad])
        

    def buscar_producto(self,nombre):
        for sublista in self.inventario:
            if nombre in sublista:
                encontrado = True
                return "Se ha encontrado el elemento"
            else:
                return "No se ha encontrado el elemento"

    def calcular_valor_inventario(self):
        for sublista in self.inventario:
            suma+=super.calcular_valor_total(sublista)

    def listar_prodcutos(self):
        return self.inventario
            
def solicitar_parametro(nombre_parametro, tipo_dato):
    """
    Solicita al usuario un valor para un parámetro específico,
    validando el tipo de dato.
    """
    while True:
        try:
            entrada = input(f"Por favor, ingrese {nombre_parametro} ({tipo_dato.__name__}): ")
            valor_convertido = tipo_dato(entrada)
            return valor_convertido
        except ValueError:
            print(f"Error: La entrada no es un {tipo_dato.__name__}. Intente de nuevo.")

def menu_principal():
    salir=False
    while not salir:
        print("""
            Por favor, elige una opción:
            1. Agregar producto
            2. Buscar producto
            3. Actualizar precio
            4. Actualizar cantidad
            5. Salir
            """)
        # Leer la opción del usuario
        eleccion = input("Ingresa el número de tu elección: ")

        # Utilizar if/elif/else para ejecutar la acción según la elección
        if eleccion == "1":
            print("Has elegido la opción agregar prodcuto.")
            nombre=solicitar_parametro("nombre", str)
            precio=solicitar_parametro("precio", int)
            cantidad=solicitar_parametro("cantidad", int)
            inventario.agregar_producto(nombre,precio,cantidadproducto)
        elif eleccion == "2":
            print("Has elegido la opción buscar prodcuto.")
            nombre=solicitar_parametro("nombre", int)
            if inventario.buscar_producto(nombre):
                print ("Producto en inventario")
            else:
                print ("Producto no existente")          
        elif eleccion == "3":
            print("Has elegido la opción actualizar precio")
            nombre=solicitar_parametro("nombre", int)
            precio=solicitar_parametro("precio", int)
            inventario.actualizar_precio(nombre,precio)
        elif eleccion == "4":
            print("Has elegido la opción actualizar cantidzd")
            nombre=solicitar_parametro("nombre", int)
            precio=solicitar_parametro("cantidad", int)
            inventario.actualizar_cantidad(nombre,cantidad)
        elif eleccion == "5":
            salir=True
            print("Programa finalizado")
        else:
            print("Opción no válida. Por favor, elige entre 1, 2, 3, 4 o 5.")

if __name__ == "__main__":
    inventario=Inventario()
    menu_principal()

