# Clase Hijo
from FigurasGeometricas import FiguraGeometrica as FiguraG
from Colores import Color


class Cuadrado(FiguraG, Color):
    def __init__(self, lado, color):
        FiguraG.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcularArea(self):
        return self.getAlto * self.getAncho

    def __str__(self):
        return f'{FiguraG.__str__(self)} {Color.__str__(self)}'