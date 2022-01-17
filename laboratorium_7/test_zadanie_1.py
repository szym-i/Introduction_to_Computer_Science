#from multiprocessing.managers import ValueProxy
import unittest
import zadanie_1

class TestZadanie11(unittest.TestCase):

    def test_operacja_zamiany(self): #test czy funkcja dobrze liczy
        self.assertEqual(zadanie_1.operacja_zamiany(2,8,"1111"),'17')
        self.assertEqual(zadanie_1.operacja_zamiany(2,10,"1111"),'15')
        self.assertEqual(zadanie_1.operacja_zamiany(2,16,"1111"),'F')
        self.assertEqual(zadanie_1.operacja_zamiany(8,2,"777"),'111111111')
        self.assertEqual(zadanie_1.operacja_zamiany(8,10,"777"),'511')
        self.assertEqual(zadanie_1.operacja_zamiany(8,16,"777"),'1FF')
        self.assertEqual(zadanie_1.operacja_zamiany(10,2,"999"),'1111100111')
        self.assertEqual(zadanie_1.operacja_zamiany(10,8,"999"),'1747')
        self.assertEqual(zadanie_1.operacja_zamiany(10,16,"999"),'3E7')
        self.assertEqual(zadanie_1.operacja_zamiany(16,2,"AF"),'10101111')
        self.assertEqual(zadanie_1.operacja_zamiany(16,8,"AF"),'257')
        self.assertEqual(zadanie_1.operacja_zamiany(16,10,"AF"),'175')
    def test_sprawdz_liczbe(self): #test czy są podnoszone odpowiednie wyjątki
        self.assertRaises(ValueError,zadanie_1.sprawdz_liczbe, 2, '2')
        self.assertRaises(ValueError,zadanie_1.sprawdz_liczbe, 8, '8')
        self.assertRaises(ValueError,zadanie_1.sprawdz_liczbe, 10, 'A')
        self.assertRaises(ValueError,zadanie_1.sprawdz_liczbe, 16, 'G')
    def test_sprawdz_systemy(self): #test wyjątków v2
        self.assertEqual(zadanie_1.sprawdz_systemy(2,2), 'co robisz')
        self.assertRaises(Exception,zadanie_1.sprawdz_systemy, 1, 11)
        self.assertRaises(Exception,zadanie_1.sprawdz_systemy, 2, 11)
        self.assertRaises(Exception,zadanie_1.sprawdz_systemy, 1, 10)
if __name__ == '__main__':
    unittest.main()