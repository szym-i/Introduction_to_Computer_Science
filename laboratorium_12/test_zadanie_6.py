import unittest
import zadanie_6

class TestZadanie6(unittest.TestCase):

    def test_Max(self):
        dane = [(0,1),(0,6),(4,1),(4,6),(9,1),(9,6),(0,7),(4,7),(9,7)]
        result = zadanie_6.Look4Rectangle(dane)
        self.assertEqual(result,5)
if __name__ == '__main__':
    unittest.main()