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
    # Creamos una lista vacía llamada 'ordenes' para almacenar las órdenes de compra.
    ordenes = []

    # Iniciamos un bucle 'while' infinito. Este bucle se ejecutará continuamente hasta que se rompa explícitamente.
    while True:
        # Llamamos a la función 'crear_computadora()' para crear una instancia de una computadora.
        computadora = crear_computadora()

        # Creamos una instancia de la clase 'Orden' que contiene la computadora creada en el paso anterior.
        orden = Orden([computadora])  # Crear una nueva orden

        # Agregamos la orden recién creada a la lista 'ordenes'.
        ordenes.append(orden)

        # Solicitamos al usuario si desea agregar otra computadora a la orden. La respuesta se almacena en la variable 'opcion' en minúsculas.
        opcion = input("¿Desea agregar otra computadora a la orden? (s/n): ").lower()

        # Comprobamos si la respuesta del usuario no es 's' (lo que significa que no desea agregar más computadoras).
        if opcion != 's':
            # Si la respuesta no es 's', salimos del bucle 'while' con 'break'.
            break

    # Iniciamos un bucle 'for' que recorre cada orden en la lista 'ordenes'.
    for orden in ordenes:
        # Imprimimos el ID de cada orden utilizando el método 'getIdOrden()' (asumiendo que existe).
        print(f"Orden de compra {orden.getIdOrden}")
