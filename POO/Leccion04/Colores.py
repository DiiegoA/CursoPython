# Clase Padre
class Color:
    def __init__(self, color):
        self._color = color

    @property
    def getColor(self):
        return self._color

    # @getColor.setter
    # def setAncho(self, color):
    #     self._color = color

    def __str__(self):
        return f'Color [color: {self._color}]'
