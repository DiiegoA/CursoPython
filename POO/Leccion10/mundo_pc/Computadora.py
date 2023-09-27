from Monitor import Monitor
from Auriculares import Auriculares
from Impresora import Impresora
from Mouse import Mouse
from Teclado import Teclado
from Escaner import Escaner


class Computadora:

  contador_computadoras = 0

  def __init__(self, nombre, monitor, auriculares, impresora, mouse, teclado, escaner):

    Computadora.contador_computadoras += 1
    self._id_computadora = Computadora.contador_computadoras
    self._nombre = nombre
    self._monitor = monitor
    self._auriculares = auriculares
    self._impresora = impresora
    self._mouse = mouse
    self._teclado = teclado
    self._escaner = escaner

  def __str__(self):
    return f'''
    {self._nombre}: {self._id_computadora}
    Monitor: {self._monitor}
    Auriculares: {self._auriculares}
    Impresora: {self._impresora}
    Mouse: {self._mouse}
    Teclado: {self._teclado}
    Escaner: {self._escaner}
    '''

# if __name__ == '__main__':

#   monitor1 = Monitor('HP', 'HDMI', '20 Pulgadas')
#   auriculares1 = Auriculares('SONY', 'Conector de audio')
#   impresora1 = Impresora('HP', 'USB')
#   mouse1 = Mouse('HP', 'USB')
#   teclado1 = Teclado('HP', 'USB')
#   escaner1 = Escaner('HP', 'USB')

#   computadora1 = Computadora('HP', monitor1, auriculares1, impresora1, mouse1, teclado1, escaner1)
#   print(computadora1)

