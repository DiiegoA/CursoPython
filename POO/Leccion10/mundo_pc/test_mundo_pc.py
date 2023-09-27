from Orden import Orden
from Computadora import Computadora
from Monitor import Monitor
from Auriculares import Auriculares
from Impresora import Impresora
from Mouse import Mouse
from Teclado import Teclado
from Escaner import Escaner


# if __name__ == '__main__':

#   monitor1 = Monitor('HP', 'HDMI', '20 Pulgadas')
#   auriculares1 = Auriculares('HP', 'Conector de audio')
#   impresora1 = Impresora('HP', 'USB')
#   mouse1 = Mouse('HP', 'USB')
#   teclado1 = Teclado('HP', 'USB')
#   escaner1 = Escaner('HP', 'USB')

#   computadora1 = Computadora('HP', monitor1, auriculares1, impresora1, mouse1, teclado1, escaner1)
#   print(computadora1)


#   monitor2 = Monitor('ACER', 'HDMI', '22 Pulgadas')
#   auriculares2 = Auriculares('ACER', 'Conector de audio')
#   impresora2 = Impresora('ACER', 'USB')
#   mouse2 = Mouse('ACER', 'USB')
#   teclado2 = Teclado('ACER', 'USB')
#   escaner2 = Escaner('ACER', 'USB')

#   computadora2 = Computadora('ACER', monitor2, auriculares2, impresora2, mouse2, teclado2, escaner2)
#   print(computadora2)


#   monitor3 = Monitor('ROG', 'HDMI', '22 Pulgadas')
#   auriculares3 = Auriculares('ROG', 'Conector de audio')
#   impresora3 = Impresora('ROG', 'BLUETOOTH')
#   mouse3 = Mouse('ROG', 'BLUETOOTH')
#   teclado3 = Teclado('ROG', 'BLUETOOTH')
#   escaner3 = Escaner('ROG', 'BLUETOOTH')

#   computadora3 = Computadora('ROG', monitor3, auriculares3, impresora3, mouse3, teclado3, escaner3)
#   print(computadora2)

#   computadoras1 = [computadora1, computadora2]

#   orden1 = Orden(computadoras1)
#   print(orden1)

#   orden1.agregar_computadora(computadora3)
#   print(orden1)

def crear_computadora():
    marca = input("Ingrese la marca de la computadora: ")
    monitor = Monitor(input("Ingrese la marca del monitor: "), input("Ingrese el tipo de conexión del monitor: "), input("Ingrese el tamaño del monitor: "))
    auriculares = Auriculares(input("Ingrese la marca de los auriculares: "), input("Ingrese el tipo de conexión de los auriculares: "))
    impresora = Impresora(input("Ingrese la marca de la impresora: "), input("Ingrese el tipo de conexión de la impresora: "))
    mouse = Mouse(input("Ingrese la marca del mouse: "), input("Ingrese el tipo de conexión del mouse: "))
    teclado = Teclado(input("Ingrese la marca del teclado: "), input("Ingrese el tipo de conexión del teclado: "))
    escaner = Escaner(input("Ingrese la marca del escáner: "), input("Ingrese el tipo de conexión del escáner: "))

    computadora = Computadora(marca, monitor, auriculares, impresora, mouse, teclado, escaner)
    return computadora


if __name__ == '__main__':
    ordenes = []

    while True:
        computadora = crear_computadora()
        orden = Orden([computadora])  # Crear una nueva orden

        ordenes.append(orden)

        opcion = input("¿Desea agregar otra computadora a la orden? (s/n): ").lower()
        if opcion != 's':
            break

    for orden in ordenes:
        print(f"Orden de compra {orden._id_orden}:\n{orden}")
