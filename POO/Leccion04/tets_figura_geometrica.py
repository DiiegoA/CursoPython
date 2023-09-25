from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FigurasGeometricas import FiguraGeometrica

# figura = FiguraGeometrica()

print('Creacion de Objeto Cuadrado' .center(50, '-'))

cuagrado1 = Cuadrado(lado = 5, color = "Verde")
# cuagrado1.setAlto = -10

print(f'Calculo del area de un Cuadrado: {cuagrado1.calcularArea()}')
print(cuagrado1)

print("\n")

print('Creacion de Objeto Rectangulo' .center(50, '-'))

rectangulo1 = Rectangulo(ancho = 10, alto = 5, color = "Rojo")
# rectangulo1.setAlto = 15
# rectangulo1.setAlto = -5

print(f'Calculo del area de un Rectangulo: {rectangulo1.calcularArea()}')
print(rectangulo1)

# MRO (Method Resolution Oeder) Muestra el orden en el que se van a ejecutar las clases, Eejemplo Clase Cuadrado
print(Cuadrado.mro())