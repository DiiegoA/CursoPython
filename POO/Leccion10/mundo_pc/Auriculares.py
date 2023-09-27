# Clase Hija
from DispositivosSalida import *

class Auriculares(DispositivosSalida):

  contador_auriculares = 0

  def __init__(self, marca, tipo_entrada):

    super().__init__(marca, tipo_entrada)
    Auriculares.contador_auriculares += 1
    self._id_auriculares = Auriculares.contador_auriculares

  def __str__(self):
    return f'Id: {self._id_auriculares}, {super().__str__()}'

# if __name__ == '__main__':

#   auriculares1 = Auriculares('SONY', 'Conector de audio')
#   print(auriculares1)