class Producto:

    def __init__ (self, nombre, precio, cantidad)
        self.productos=[]

    def __str__(self)
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

