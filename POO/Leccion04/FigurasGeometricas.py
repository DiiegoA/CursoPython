# Clase Padre
# ABC = Abstract Base Class - Obliga a que sus Hijos tengan los mismo metodos del Padre
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo en el Ancho: {ancho}')

        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo en el Alto: {alto}')

    @property
    def getAncho(self):
        return self._ancho

    # @getAncho.setter
    # def setAncho(self, ancho):
    #     if self._validar_valor(ancho):
    #         self._ancho = ancho
    #     else:
    #         self._ancho = 0
    #         print(f'Valor erroneo en el Ancho: {ancho}')

    @property
    def getAlto(self):
        return self._alto

    # @getAlto.setter
    # def setAlto(self, alto):
    #     if self._validar_valor(alto):
    #         self._alto = alto
    #     else:
    #         self._alto = 0
    #         print(f'Valor erroneo en el Alto: {alto}')

    @abstractmethod
    def calcularArea(self):
        pass

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'

    def _validar_valor(self, valor):
        return True if 0 < valor <= 10 else False
