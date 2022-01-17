import unittest
import zadanie_11

lista1 = [1,2,3,45,66]
lista2 = [0,0,0,0]
lista3 = [31,45,12]
bad_lista = ['a','1']

class TestZadanie11(unittest.TestCase):

    def test_Max(self):
        self.assertEqual(zadanie_11.Max(lista1,lista1[-1],len(lista1)),66)
        self.assertEqual(zadanie_11.Max(lista2,lista2[-1],len(lista2)),0)
        self.assertEqual(zadanie_11.Max(lista3,lista3[-1],len(lista3)),45)
        self.assertRaises(Exception,zadanie_11.Max(bad_lista,bad_lista[-1],len(bad_lista)))
    def test_Suma(self):
        self.assertEqual(zadanie_11.Suma(lista1,0,len(lista1)),117)
        self.assertEqual(zadanie_11.Suma(lista2,0,len(lista2)),0)
        self.assertEqual(zadanie_11.Suma(lista3,0,len(lista3)),88)
if __name__ == '__main__':
    unittest.main()