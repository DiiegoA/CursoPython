# Ciclo While en Python
# cont = 0
#
# while cont < 3:
#     print(cont)
#     cont += 1
# else:
#     print('Fin de ciclo While!!')

# cont = 0
#
# while cont <= 5:
#     print(cont)
#     cont += 1
# else:
#     print('Fin de ciclo While!!')

# Descendeente
# cont = 5
#
# while cont >= 1:
#     print(cont)
#     cont -= 1
# else:
#     print('Fin de ciclo While!!')

# Ciclo for en Python
# cadena = 'Hola Mundo'
#
# for letra in cadena:
#     print(letra)
# else:
#     print('Fin del ciclo for')

# cadena = 'Hola Mundo'
#
# for letra in cadena:
#     if letra == 'o':
#         print(f'letra encontrada: {letra}')
#         break
# else:
#     print('Fin del ciclo for')

# for i in range(6):
#     if i % 2 == 0:
#         print(f'Valor: {i}')

# for i in range(6):
#     if i % 2 != 0:
#         continue
#     print(f'Valor: {i}')

# Iterador iter()
# libro = ['pag1', 'pag2', 'pag3']
# marca_paginas = iter(libro)
#
# print(next(marca_paginas))
# print(next(marca_paginas))
# print(next(marca_paginas))

# Iterador zip()  Une 2 listas por el mismo indice y retorna una lista que contiene tuplas con los 2 elementos del mismo indice de
# las listas
# a = [1, 2]
# b = ['Uno', 'Dos']
# c = zip(a, b)
#
# print(c)
# lisa = list(c)
#
# print(lisa)

# Añadiendo condicionales
frase = 'r con r cigarro, r con r barril'
erres = [i for i in frase if i == 'r']

print(erres)
print(len(erres))