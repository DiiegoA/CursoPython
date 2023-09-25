from Producto import Producto


class Orden:

    contador_ordenes = 0

    @classmethod
    def generar_contador_ordenes(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, productos):
        self._id_orden = Orden.generar_contador_ordenes()
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0

        for producto in self._productos:
            total += producto.getPrecio
        return total

    def __str__(self):
        productos_str = ''

        for producto in self._productos:
            productos_str += producto.__str__() + '|'

        return f'Orden: {self._id_orden}, \nProductos: {productos_str}'