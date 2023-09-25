# Funciones en Python
# def miFuncion():
#     print('Saludos desde mi funcion')
#
# miFuncion()
#
# def miFuncion1(nombre, apellidos):
#     print(f'Nombre: {nombre}, Apellidos: {apellidos}')
#
# miFuncion1('Diego', 'Aguirre')

# def sumar(a, b):
#     suma = a + b
#     return  suma
#
# print(f'Resultado de la suma: {sumar(3, 4)}')

# def sumar(a=0, b=0) -> int:  # -> int pista
#     suma = a + b
#     return suma
#
#
# print(f'Resultado de la suma: {sumar()}')
# print(f'Resultado de la suma: {sumar(5, 4)}')

# Argumentos Variables en Funciones con Python
# def listarNombres(*nombres): # Cantidad de argumentos variable
#     for nombre in nombres:   # Se convierte en una Tupla
#         print(nombre)
#
# listarNombres('Diego', 'Alejandra', 'Pacho')
# listarNombres('Fabian', 'Claudia', 'Alberto')

# def sumarNumeros(*arg):
#     result = 0
#
#     for num in arg:
#         result += num
#
#     return result
#
# print(sumarNumeros(1,2,3,4))

# def multiplicarNumeros(*arg):
#     result = 1
#
#     for num in arg:
#         result *= num
#
#     return result
#
# print(multiplicarNumeros(2,4,6,8))

# Argumentos Variables llave-valor en Python
# def listarTerminos(**terminos):  # kwargs
#     for llave, valor in terminos.items():
#         print(f'{llave}: {valor}')
#
# listarTerminos(IDE = 'Integrated Developement Environment', PK = 'Primary key')
# listarTerminos(PI = 3.1416)

# def desplegarNombres(nombres):
#     for nombre in nombres:
#         print(nombre)
#
# nombres = ['Diego', 'Pacho', 'Rufus']
# desplegarNombres(nombres)
# desplegarNombres('Aleja')
# desplegarNombres((10,)) # Si se agrega () a un número se convierte en Tupla
# desplegarNombres((10, 11))

# Funciones Recursivas en Python
# def factorial(numero):
#     if numero < 0: return print("No se pueden ingresar numero Negativos")
#
#     elif numero == 0: return 1
#
#     else: return numero * factorial(numero - 1)
#
# print(factorial(5))

# def descendente(numeros):
#
#     if numeros >= 1:
#         print(numeros)
#         descendente(numeros - 1)
#
#     elif numeros < 0:
#         print("No se pueden ingresar números Negativos")
#
# descendente(-1)

# def calculadoraImpuesto(pago_sin_impuesto, impuesto):
#     pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
#     return pago_total
#
# pago_sin_impuesto = float(input('Proporcione el pago sin impuesto: '))
# impuesto = float(input('Proporcione el monto del impuesto: '))
#
# pago_con_impuesto = calculadoraImpuesto(pago_sin_impuesto, impuesto)
# print(f'Pago con impuesto: {pago_con_impuesto}')

def celsius_a_fahrenheit(celsius):
    gradosFahrenheit = celsius * 1.8 + 32
    return gradosFahrenheit

celsius = float(input('Ingrese los grados celsius: '))

convertir_celsius_a_fahrenheit = celsius_a_fahrenheit(celsius)
print(f'La convercion de {celsius} grados celsius a fahrenheit es: {convertir_celsius_a_fahrenheit} grados fahrenheit')

def fahrenheit_a_celsius(fahrenheit):
    gradosCelsius = (fahrenheit - 32) / 1.8
    return gradosCelsius

fahrenheit = float(input('Ingrese los grados fahrenheit: '))

convertir_fahrenheit_a_celsius = fahrenheit_a_celsius(fahrenheit)
print(f'La convercion de {fahrenheit} grados fahrenheit  a celsius es: {convertir_fahrenheit_a_celsius} grados celsius')


# fahrenheit = convertir_celsius_a_fahrenheit
#
# def fahrenheit_a_celsius(fahrenheit):
#     gradosCelsius = (fahrenheit - 32) / 1.8
#     return gradosCelsius
#
# convertir_fahrenheit_a_celsius = fahrenheit_a_celsius(fahrenheit)
# print(f'La convercion de {fahrenheit} grados fahrenheit  a celsius es: {convertir_fahrenheit_a_celsius} grados celsius')
