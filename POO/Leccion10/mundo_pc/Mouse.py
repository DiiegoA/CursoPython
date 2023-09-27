# Clase Hija
from DispositivosEntrada import *

class Mouse(DispositivosEntrada):

  contador_mouse = 0

  def __init__(self, marca, tipo_entrada):

    Mouse.contador_mouse += 1
    self._id_mouse = Mouse.contador_mouse
    super().__init__(marca, tipo_entrada)

  def __str__(self):
    return f'Id: {self._id_mouse}, {super().__str__()}'


# if __name__ == '__main__':

#   mouse1 = Mouse('HP', 'USB')
#   print(mouse1)