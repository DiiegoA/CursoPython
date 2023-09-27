# Clase Hija
from DispositivosSalida import *

class Monitor(DispositivosSalida):

  contador_monitor = 0

  def __init__(self, marca, tipo_entrada, tamano):

    super().__init__(marca, tipo_entrada)
    Monitor.contador_monitor += 1
    self._id_monitor = Monitor.contador_monitor
    self._tamano = tamano

  def __str__(self):
    return f'Id: {self._id_monitor}, {super().__str__()}, Tamaño: {self._tamano}'

# if __name__ == '__main__':

#   monitor1 = Monitor('ACER', 'HDMI', '32 Pulgadas')
#   print(monitor1)