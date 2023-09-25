class Persona:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  # Sobrecargar el operador add(Suma)
  def __add__(self, other):
    return f'{self.nombre} {other.nombre}'

    # Sobrecargar el operador sub(Resta)
  def __sub__(self, other):
    return self.edad - other.edad


persona1 = Persona("Juan", 15)
persona2 = Persona("Diego", 28)

print(persona1 + persona2)
print(persona1 - persona2)