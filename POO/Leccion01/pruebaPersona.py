# Uso de Módulos y Clases en Python

from Persona import Persona

print('Creacion Objetos'.center(40,'-'))

persona2 = Persona('Poca', 'Cosa', 8)
persona2.mostrar_detalle()

# Destructor de Objetos en Python
# Se llama la funcion del desde la clase Persona

print('Eliminacion Objetos'.center(40,'-'))
del persona2