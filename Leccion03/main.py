# Sentencia If/Else en Python
# condicion = False
#
# if condicion == True:
#     print('La condicion es Verdadera')
# elif condicion == False:
#     print('La condicion es Falsa')
# else:
#     print('la condicion no coincide')

# numero = int(input('Ingrese un numero del 1 al 3: '))
# numeroTexto = ''
#
# if numero == 1:
#     numeroTexto = 'Número uno'
# elif numero == 2:
#     numeroTexto = 'Número dos'
# elif numero == 3:
#     numeroTexto = 'Número tres'
# else:
#     numeroTexto = 'Número fuera de rango'
#
# print(f'Número proporcionado: {numero}: {numeroTexto}')

#  Sintáxis if else simplificada (Operador Ternario)
# condicion = True
#
# print('Condición Verdadera') if condicion else print('Condición Falsa')

# mes = int(input('Ingresa el mes del año (1 al 12: '))
#
# estacion = None
#
# if mes == 12 or mes == 1 or mes == 2:
#     estacion = 'Invierno'
# elif mes == 3 or mes == 4 or mes == 5:
#     estacion = 'Primavera'
# elif mes == 6 or mes == 7 or mes == 8:
#     estacion = 'Verano'
# elif mes == 9 or mes == 10 or mes == 11:
#     estacion = 'Otoño'
# else:
#     estacion = 'No existe'
#
# print(f'Para el mes {mes} la estación del año es: {estacion}')

# edad = int(input('Ingresa tu edad: '))
#
# etapa = None
#
# if 0 <= edad <= 10:
#     etapa = 'La infancia es Increible...'
# elif 10 < edad <= 20:
#     etapa = 'Muchos cambios y mucho estudio...'
# elif 20 < edad <= 30:
#     etapa = 'Amor y mucho trabajo...'
# else:
#     etapa= 'Esta etapa de vida no es reconocida!!'
#
# print(f'A la edad de {edad}, su etapa de vida: {etapa} ')

# nota = int(input('Ingrese la nota del (1 al 10): '))
# letra = None
#
# if nota == 9 or nota == 10:
#     letra = 'A'
# elif 8 <= nota < 9:
#     letra = 'B'
# elif 7 <= nota < 8:
#     letra = 'C'
# elif 6 <= nota < 7:
#     letra = 'D'
# elif 0 <= nota < 6:
#     letra = 'F'
# else:
#     letra = 'Valor Incorrecto!!'
#
# print(f'Su nota es de: {letra}')

# Ciclo While en Python