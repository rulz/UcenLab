def hola():
    msg = 'Hola Muchachos'
    return msg

class PersonaClassBase(object):
    def __init__(self, nombre):
        self.nombre = nombre

class PersonaClass(PersonaClassBase):
    def __init__(self, nombre, apellido):
        super(PersonaClass, self).__init__(nombre)
        self.apellido = apellido

    def obtener_nombre_completo(self):
        return '{0} {1}'.format(self.nombre, self.apellido)

class Mat(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num2 + self.num1

    def resta(self):
        return self.num2 - self.num1

    def mult(self):
        return self.num2 * self.num1

    def div(self):
        return self.num2 / self.num1
