from Orden import Orden
from Producto import Producto

producto1 = Producto("Camisa", 50.00)
producto2 = Producto("Sombrero", 200.00)
producto3 = Producto("Zapatos", 100.00)
producto4 = Producto("Corbata", 15.00)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(f"Total de la Orden1 = {orden1.calcular_total()}")

orden2 = Orden(productos2)
orden2.agregar_producto(producto1)
orden2.agregar_producto(producto2)
print(orden2)
print(f"Total de la Orden2 = {orden2.calcular_total()}")
