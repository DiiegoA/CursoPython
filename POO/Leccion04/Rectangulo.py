# Clase Hijo
from FigurasGeometricas import FiguraGeometrica as FiguraG
from Colores import Color


class Rectangulo(FiguraG, Color):
    def __init__(self, ancho, alto, color):
        FiguraG.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcularArea(self):
        return self.getAlto * self.getAncho

    def __str__(self):
        return f'{FiguraG.__str__(self)} {Color.__str__(self)}'
