# Clase Hija
from DispositivosSalida import *

class Impresora(DispositivosSalida):

  contador_impresora = 0

  def __init__(self, marca, tipo_entrada):

    super().__init__(marca, tipo_entrada)
    Impresora.contador_impresora += 1
    self._id_impresora = Impresora.contador_impresora

  def __str__(self):
    return f'Id: {self._id_impresora}, {super().__str__()}'

# if __name__ == '__main__':

#   impresora1 = Impresora('HP', 'USB')
#   print(impresora1)