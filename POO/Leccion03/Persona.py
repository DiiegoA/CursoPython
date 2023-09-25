# Clase Padre

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Sobreescritura del método __str__() en Python
    def __str__(self):
        return f'Persona: (Nombre : {self._nombre}, Edad: {self._edad})'


# Clase Hija que Hereda atributos de la Clase Padre

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    # Sobreescritura del método __str__() en Python
    def __str__(self):
        return f'{super().__str__()}, Sueldo: {self._sueldo}'


if __name__ == '__main__':
    empleado1 = Empleado('Diego', 28, 5000)
    print(empleado1._nombre)


