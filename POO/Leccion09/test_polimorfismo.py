from Empleado import Empleado
from Gerente import Gerente

def imprimirDetalles(object):
  #print(object)
  print(type(object))

  # Polimorfismo
  print(object.mostrarDetalles())

  if isinstance(object, Gerente):

    print(object.departamento)


empleado = Empleado('Diego', 5000)
imprimirDetalles(empleado)

gerente1 = Gerente('Juan', 10000, 'IT')
imprimirDetalles(gerente1)