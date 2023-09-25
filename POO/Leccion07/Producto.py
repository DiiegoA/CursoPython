class Producto:

    contador_productos = 0

    @classmethod
    def generar_contador_productos(cls):
        cls.contador_productos += 1
        return cls.contador_productos

    def __init__(self, nombre, precio):
        self._id_producto = Producto.generar_contador_productos()
        self._nombre = nombre
        self._precio = precio

    @property
    def getIdProducto(self):
        return self._id_producto

    @property
    def getNombre(self):
        return self._nombre

    @property
    def getPrecio(self):
        return self._precio

    def __str__(self):
        return f'Producto [Id: {self._id_producto}, Nombre: {self._nombre}, Precio : {self._precio}]'


if __name__ == '__main__':

    producto1 = Producto('Camisa', 50.00)
    print(producto1)

    producto2 = Producto('Zapatos', 100.00)
    print(producto2)