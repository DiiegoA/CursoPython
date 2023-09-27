# Clase Padre

class DispositivosEntrada:


  def __init__(self, marca, tipo_entrada) :

    self._marca = marca
    self._tipo_entrada = tipo_entrada

  def __str__(self):
    return f'Marca: {self._marca}, Tipo de entrada: {self._tipo_entrada}'

  # Polimorfismo
  def mostrarDetalles(self):
    return self.__str__()