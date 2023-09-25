# Clase padre
class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return f' \nColor: {self._color} \nRuedas: {self._ruedas}'


# Clses Hija
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    # Sobreescritura del método __str__() en Python
    def __str__(self):
        return f'Coche: {super().__str__()} \nVelocidad: {self._velocidad} Km/h \n'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo_bicicleta):
        super().__init__(color, ruedas)
        self._tipo = tipo_bicicleta

    # Sobreescritura del método __str__() en Python
    def __str__(self):
        return f'Bicicleta: {super().__str__()} \nTipo de Bicicleta: {self._tipo}'
