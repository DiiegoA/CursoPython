# Clase Hija
from DispositivosEntrada import *

class Teclado(DispositivosEntrada):

  contador_teclado = 0

  def __init__(self, marca, tipo_entrada):

    super().__init__(marca, tipo_entrada)
    Teclado.contador_teclado += 1
    self._id_teclado = Teclado.contador_teclado

  def __str__(self):
    return f'Id: {self._id_teclado}, {super().__str__()}'

# if __name__ == '__main__':

#   teclado1 = Teclado('ACER', 'USB')
#   print(teclado1)