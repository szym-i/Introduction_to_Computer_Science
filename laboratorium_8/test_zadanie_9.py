import unittest
import zadanie_9

class TestZadanie11(unittest.TestCase):

    def test_generuj(self):
        self.assertEqual(zadanie_9.generuj(10),([6], [4, 9]))
        self.assertEqual(zadanie_9.generuj(50),([6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46], [4, 9, 25, 49]))
        self.assertEqual(zadanie_9.generuj(100),([6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95], [4, 9, 25, 49]))
if __name__ == '__main__':
    unittest.main()