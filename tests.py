import unittest
from scripts import hola, PersonaClassBase, PersonaClass, Mat


class HolaTest(unittest.TestCase):

    def test_mensaje(self):
        self.assertEqual('Hola Muchachos', hola())

class PersonaClassBaseTest(unittest.TestCase):

    def test_nombre(self):
        persona = PersonaClassBase('Raul')
        self.assertEqual('Raul', persona.nombre)

class PersonaClassTest(unittest.TestCase):

    def test_nombre(self):
        persona = PersonaClass('raul','setron')
        self.assertEqual('raul', persona.nombre)
        self.assertEqual('setron', persona.apellido)
        self.assertEqual('raul setron', persona.obtener_nombre_completo())

class MatClassTest(unittest.TestCase):

    def test_numeros(self):
        mat = Mat(1, 2)
        self.assertNotEqual(mat.num1, 2)
        self.assertEqual(mat.num1, 1)
        self.assertNotEqual(mat.num2, 1)
        self.assertEqual(mat.num2, 2)

    def test_suma(self):
        mat = Mat(1, 2)
        self.assertEqual(mat.suma(), 3)

    def test_resta(self):
        mat = Mat(1, 2)
        self.assertNotEqual(mat.resta(), 3)
        self.assertEqual(mat.resta(), 1)

    def test_mult(self):
        mat = Mat(1, 2)
        self.assertEqual(mat.mult(), 2)

    def test_div(self):
        mat = Mat(1, 2)
        self. assertEqual(mat.div(), 2)

if __name__ == '__main__':
    unittest.main()
