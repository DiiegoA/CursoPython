# Clase Hija
from DispositivosEntrada import *

class Escaner(DispositivosEntrada):

  contador_escaner = 0

  def __init__(self, marca, tipo_entrada):

    Escaner.contador_escaner += 1
    self._id_escaner = Escaner.contador_escaner
    super().__init__(marca, tipo_entrada)

  def __str__(self):
    return f'Id: {self._id_escaner}, {super().__str__()}'


# if __name__ == '__main__':

#   escaner1 = Escaner('', 'USB')
#   print(escaner1)