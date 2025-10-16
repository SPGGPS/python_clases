
class Producto:
    def __init__ (self, nombre, precio, cantidad):
        pass

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"

    def agregar (self,nombre,precio,cantidades):
        if self.nombre != "":
            self.nombre=str(nombre)
        else:
            raise ValueError("Nombre vacios.")
        if self.precio > 0:
            self.precio=float(precio)
        else:
            raise ValueError("Precio negativo o cero")
        if self.cantidad > 0:
            self.cantidad=int(cantidad)
        else:
            raise ValueError("Cantidad negativa o cero")

    def actualizar_precio(self,nuevo_precio):
        if nuevo_precio > 0:
            self.precio=nuevo_precio

    def actualizar_cantidad(self,nueva_cantidad):
        if nueva_cantidad > 0:
            self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.canitad

class Inventario (Producto)
    def __init__ (self):
        inventario = []

    def agregar_producto(self,producto):
        self.inventario.append([self.producto.nombre,self.producto.precio,self.producto.cantidad)
        

    def buscar_producto(self,nombre):
        for sublista in self.inventario:
            if nombre in sublista:
                encontrado = True
                return "Se ha encontrado el elemento"
            else:
                return "No se ha encontrado el elemento"

    def calcular_valor_inventario(self):
        for sublista in self.inventario:
            suma+=sublista[1]*sublista[2]

    def listar_prodcutos(self)
        return self.inventario
            

def menu_principal():
    salir=False
    while not salir:
        print("""
            Por favor, elige una opción:
            1. Agregar producto
            2. Buscar producto
            3. Actualizar producto
            4. Actualizar cantidad
            5. Salir
            """)
        # Leer la opción del usuario
        eleccion = input("Ingresa el número de tu elección: ")

        # Utilizar if/elif/else para ejecutar la acción según la elección
        if eleccion == "1":
            print("Has elegido la Opción A.")
            
        elif eleccion == "2":
            print("Has elegido la Opción B.")
        elif eleccion == "3":
            print("Has elegido la Opción C.")
        elif eleccion == "3":
            print("Has elegido la Opción C.")
        elif eleccion == "5":
            salir=True
        else:
            print("Opción no válida. Por favor, elige entre 1, 2, 4 o 5.")

if __name__ == "__main__":
    inventario=Inventario()
    menu_principal()

