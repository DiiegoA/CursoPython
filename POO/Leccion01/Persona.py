# class Persona:
#
#     def __init__(self):
#         self.nombre = 'Diego'
#         self.apellido = 'Aguirre'
#         self. edad = 28
#
# persona1 = Persona()
#
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

# class Persona:
#
#     def __init__(self, name, lastname, age):
#         self.nombre = name
#         self.apellido = lastname
#         self. edad = age
#
# persona1 = Persona('Diego', 'Aguirre', 28)
#
# print(f'Objeto persona 1 : nombre y apellido: {persona1.nombre} {persona1.apellido} edad: {persona1.edad}')

# Modificar Atributos de un Objeto
# persona1.nombre = 'Rosa'
# persona1.apellido = 'Ortiz'
# persona1.edad = 83
#
# print(f'Objeto persona 1 : nombre y apellido: {persona1.nombre} {persona1.apellido} edad: {persona1.edad}')
#
# persona2 = Persona('Clemencia', 'Aguirre', 51)
#
# print(f'Objeto persona 2 : nombre y apellido: {persona2.nombre} {persona2.apellido} edad: {persona2.edad}')

# class Persona:
#
#     def __init__(self, name, lastname, age):
#         self.nombre = name
#         self.apellido = lastname
#         self. edad = age
#
#     def mostrar_detalle(self):
#         print(f'Persona : nombre y apellido: {self.nombre} {self.apellido} edad: {self.edad}')
#
# persona1 = Persona('Diego', 'Aguirre', 28)
# persona1.mostrar_detalle()
#
# # Agregar un elemento a un objeto especifico
# persona1.telefono = 3115487521
#
# print(persona1.telefono)
#
# persona2 = Persona('Clemencia', 'Aguirre', 51)
# persona2.mostrar_detalle()


# class Persona:
#
#     def __init__(self, nombre, apellido, edad, *tupla, **diccionario):
#         self.nombre = nombre
#         self.apellido = apellido
#         self. edad = edad
#         self.tupla = tupla
#         self.diccionario = diccionario
#
#     def mostrar_detalle(self):
#         print(f'Persona : nombre y apellido: {self.nombre} {self.apellido} edad: {self.edad}, {self.tupla}, {self.diccionario}')
#
# persona1 = Persona('Diego', 'Aguirre', 28, '3113698574', 2, 3, 4, m = 'Mango', k = 'Kiwwi')
# persona1.mostrar_detalle()
#
# persona2 = Persona('Clemencia', 'Aguirre', 51)
# persona2.mostrar_detalle()

# class Persona:
#
#     def __init__(self, nombre, apellido, edad,):
#         self.__nombre = nombre
#         self._apellido = apellido
#         self._edad = edad
#
#
#     def mostrar_detalle(self):
#         print(f'Persona : nombre y apellido: {self.__nombre} {self._apellido} edad: {self._edad}')
#
# persona1 = Persona('Diego', 'Aguirre', 28)
# persona1.__nombre = 'Sergio'  # Poniendo __ al atributo nombre no se puede modificar su contenido
#
# persona1.mostrar_detalle()


#Métodos Get y Set en Python

# Get = Obtener o Recuperar
# Set = Colocar o Modificar

# class Persona:
#
#     def __init__(self, nombre, apellido, edad,):
#         self._nombre = nombre
#         self._apellido = apellido
#         self._edad = edad
#
#     @property
#     def getNombre(self):
#         return self._nombre
#
#     @getNombre.setter
#     def setNombre(self, nombre):
#         self._nombre = nombre
#
#     def mostrar_detalle(self):
#         print(f'Persona : nombre y apellido: {self._nombre} {self._apellido} edad: {self._edad}')
#
# persona1 = Persona('Diego', 'Aguirre', 28)
# print(persona1.getNombre)
#
# persona1.setNombre = 'Diego Felipe'
# print(persona1.getNombre)

# Atributos read-only (sólo lectura) en Python
#
# class Persona:
#
#     def __init__(self, nombre, apellido, edad,):
#         self._nombre = nombre
#         self._apellido = apellido
#         self._edad = edad
#
#     @property
#     def getNombre(self):
#         return self._nombre
#
#     # @getNombre.setter
#     # def setNombre(self, nombre):
#     #     self._nombre = nombre
#
#     def mostrar_detalle(self):
#         print(f'Persona : nombre y apellido: {self._nombre} {self._apellido} edad: {self._edad}')
#
# persona1 = Persona('Diego', 'Aguirre', 28)
# print(persona1.getNombre)
#
# persona1.getNombre = 'Diego Felipe'
# print(persona1.getNombre)

# Encapsulando todos los Atributos de una Clase
class Persona:

    def __init__(self, nombre, apellido, edad,):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def getNombre(self):
        return self._nombre

    @getNombre.setter
    def setNombre(self, nombre):
        self._nombre = nombre

    @property
    def getApellido(self):
        return self._apellido

    @getApellido.setter
    def setApellido(self, apellido):
        self._apellido = apellido

    @property
    def getEdad(self):
        return self._edad

    @getEdad.setter
    def setEdad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona : nombre y apellido: {self._nombre} {self._apellido} edad: {self._edad}')

    def __del__(self):
        print(f'{self._nombre} {self._apellido}')

if __name__ == '__main__':

    persona1 = Persona('Diego', 'Aguirre', 28)
    print(persona1.getNombre)

    persona1.setNombre = 'Diego Felipe'
    print(persona1.getNombre)

    print(persona1.getApellido)

    persona1.setApellido = 'Aguirre López'
    print(persona1.getApellido)

    print(persona1.getEdad)

    persona1.setEdad = 30
    print(persona1.getEdad)

    persona1.mostrar_detalle()

    print(__name__)