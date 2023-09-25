class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)


MiClase.metodo_estatico()
MiClase.metodo_clase()

objeto1 = MiClase('Valor variable instancia')
objeto1.metodo_clase()
objeto1.metodo_instancia()



# print(MiClase.variable_clase)
#
# miClase1 = MiClase('Valor variable instancia')
# print(miClase1.variable_instancia)
# print(miClase1.variable_clase)
#
# MiClase.variable_clase2 = 'Valor variable clase 2'
#
# miClase2 = MiClase('Otro valor variable instancia')
# print(miClase2.variable_instancia)
# print(miClase2.variable_clase)
# print(MiClase.variable_clase2)
# print(miClase1.variable_clase2)
# print(miClase2.variable_clase2)