class Cubo:

    def __init__(self, ancho, profundidad, alto):
        self.ancho = ancho
        self.profundidad = profundidad
        self.alto = alto

    def calcular_volumen(self):
        return self.ancho * self.profundidad * self.alto

ancho = int(input('Proporcione el ancho: '))
profundidad = int(input('Proporcione la profundidad: '))
alto = int(input('Proporcione el alto: '))

cubo1 = Cubo(ancho, profundidad, alto)
print(f'Volúmen cubo: {cubo1.calcular_volumen()}')