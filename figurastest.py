
import unittest
from figuras import Figuras

class TestFiguras(unittest.TestCase):

    def setUp(self):
         self.figura = Figuras()
    
    def test_area_cuadrado_lado_5(self):
       
        resultado= self.figura.cuadrado(5)
        self.assertEquals(25,resultado)

    def test_area_cuadrado_lado_6(self):
        resultado= self.figura.cuadrado(6)
        self.assertEquals(36,resultado)

    def test_area_cuadrado_lado_g(self):
        resultado= self.figura.cuadrado('g')

        self.assertEquals('dato incorrecto',resultado)
       
    def test_area_cuadrado_lado_siete(self):
        resultado= self.figura.cuadrado(7)

        self.assertEquals(49,resultado)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main() 
