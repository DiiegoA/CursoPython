# Lista de String
# nombres = ['Diego', 'Pacho', 'Aleja', 'Fabian']
#
# print(nombres)
# print(nombres[1])
# # Acceder al ultimo valor del ultimo indice
# print(nombres[-1])
#
# Mostrar el indice de un elemento
# print(nombres.index('Aleja'))

# Acceder al elemnto de una lista dentro de otra lista
# newNombres = ['Stella', 'Adriana', 'Sofia']
# nombres.append(newNombres)
#
# print(nombres)
# print(nombres[4][2])

# # Acceder a un rango de la lista entre el indice 0 y 1
# print(nombres[0:2])
#
# # Acceder a un rango de la lista entre el primer indice y el indice 2
# print(nombres[:3])
#
# # Acceder a un rango de la lista entre el indice 2 y el indice final
# print(nombres[2:])
#
# Revisar si un elemento esta presente
# print('Diego' in nombres)
#
# # Cambiar valor de la lista
#
# nombres[1] = 'Marley'
# print(nombres)
#
# for nombre in nombres:
#     print(nombre)
# else:
#     print('No existen mas nombres en la lista')

# Imprimir el largo de la lista
# nombres = ['Diego', 'Pacho', 'Aleja', 'Fabian']
#
# print(len(nombres))
#
# nombres.append('Marley')
#
# print(nombres)
#
# Insertar un elemento en un indice especifico
# nombres.insert(1, 'Rosa')
#
# print(nombres)
#
# Agregar varios elementos a la lista
# otrsoNombres = ['Claudia', 'Oscar', 'Jero']
# nombres.extend(otrsoNombres)
#
# print(nombres)

# Ordenar la lista
# num = [0,2,8,4,6,5,3,1]
#
# print(num.sort())
#
# nombres.sort()
#
# print(nombres)
#
# nombres.sort(reverse=True)
#
# print(nombres)
#
# Mostrar cuantos elementos estan repetidos
# repetidos = nombres * 4
# repetidos.sort()
#
# print(repetidos)
#
# for element in set(repetidos):   # Utilizamos la función set() para obtener un conjunto de elementos únicos en la lista.
#     count = repetidos.count(element)
#     print(f'{element} aparece {count} veces en la lista.')
#
# Covertir un rango en una lista
# rango = range(1,21)
# lista = list(rango)
#
# print(lista)
#
# Eliminar un elemento
# nombres.remove('Diego')
#
# print(nombres)
#
# # Eliminar el ultimo valor
# nombres.pop()
#
# print(nombres)
#
# Extraer el ultimo elemento de la lista y guardarlo en una variable
# ulti_elem = nombres.pop()
#
# print(ulti_elem)
#
# Eliminar un Indice
# del nombres[0]
#
# print(nombres)
#
# # limpiar lista
# nombres.clear()
#
# print(nombres)
#
# # Borrar la lista por completo
# del nombres
#
# print(nombres)
#
# Sintaxis de range (inicio <Opcional>, fin <Opcional>, incremento <Opcional>)
# for i in range(0, 10, 3):
#     print(i)
#
# print('Rango con valores de Inicio y Fin')
#
# for i in range(2, 6 + 1):
#     print(i)
#
# print('Rango con valores de Inicio, Fin y Salto')
#
# for i in range(3, 11, 2):
#     print(i)

# Tuplas en Python, Una Tupla es una lista que no se puede modificar
# frutas = ('Naranja',)  Si es un solo valor de uan Tupla se debe terminar con una ','
# frutas = ('Naranja', 'Manzana', 'Fresa')
# print(frutas)
#
# # Imprimir el rango
# print(len(frutas))
#
## revisar si un elemento esta presente
# print('Manzana' in frutas)
#
# # Acceder a un elemento
# print(frutas[0])
#
# # Acceder al ultimo elemento
# print(frutas[-1])
#
# # Acceder a un rango
# print(frutas[:1])
# print(frutas[1:])
#
# # Recorrer Elementos
# for fruta in frutas:
#     print(fruta, end=', ')
#
# # Cambiar valor a la Tupla
# # frutas[0] = 'Pera'
# # print(frutas)
#
# listaFrutas = list(frutas)
# listaFrutas[0] = 'Pera'
# frutas = tuple(listaFrutas)
#
# print('\n', frutas)

# Imprime cuantos valores hay repetidos
# mi_tuplas = (1,2,3,3)
# print(mi_tuplas.count(3))
#
# Covertir un rango en una tupla
# rango = range(1,21)
# tupla = tuple(rango)
#
# print(tupla)
#
# # Eliminar la Tupla
# del frutas
# print(frutas)

# Dada la siguiente Tupla, crear una lista que solo incluya los número menores a 5
# tupla = (13, 1, 8, 3, 2, 5, 8)
#
# newList = []
#
# for list in tupla:
#     if list < 5:
#         newList.append(list)
#
# print(newList)

# set
# planetas = {'Jupiter', 'Venus', 'Marte'}
# print(planetas)
#
# # Imprimir el rango
# print(len(planetas))
#
# # revisar si un elemento esta presente
# print('Marte' in planetas)
#
# # Agregar un elemento
# planetas.add('Tierra')
# print(planetas)
#
# # No se pueden duplicar elementos
# planetas.add('Tierra')
# print(planetas)
#
# # Eliminar un elemento, puede arrojar un error si no encuentra el elemento
# planetas.remove('Tierra')
# print(planetas)
#
# # Eliminar un elemento sin arrojar un errores
# planetas.discard('Marte')
# print(planetas)
#
# # Limpiar set
# planetas.clear()
# print(planetas)
#
# # Eliminar por completo al set
# del planetas
# print(planetas)

# Diccionarios en Python (key, value)
# diccionario = {
#     'IDE': 'Integrated Development Environment',
#     'OOP': 'Object Oriented Programming',
#     'DBMS': 'Database Management System'
# }
#
# print(diccionario)
#
# # Imprimir el rango
# print(len(diccionario))
#
# # Acceder a un elemento (key)
# print(diccionario['IDE'])
#
# # Otra forma de acceder a un elemento
# print(diccionario.get('OOP'))
#
# # Modificar elemento
# diccionario['IDE'] = 'integrated development environment'
# print(diccionario)
#
# # Recorrer los elementos
# for llaves, valor in diccionario.items():
#     print(llaves, valor)
#
# for llaves in diccionario.keys():
#     print(llaves)
#
# for valor in diccionario.values():
#     print(valor)
#
# # Comprobar existencia de un elemenrto
# print('OOP' in diccionario)
#
# # Agregar un elemento
# diccionario['PK'] = 'Primary Key'
# print(diccionario)
#
# # Remover un elemento
# diccionario.pop('DBMS')
# print(diccionario)
#
# # Limpiar
# diccionario.clear()
# print(diccionario)
#
# # Eliminar por completo
# del diccionario
# print(diccionario)