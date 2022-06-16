from pickletools import string1
import unittest
from uzduotis1 import skaiciu_suma, saraso_suma, didziausias_skaicius, stringas_atbulai, info_apie_sakini

class TestUzduotis(unittest.TestCase):
     def test_skaiciu_suma(self):
        self.assertEqual(8, skaiciu_suma(2, 2, 4)) 
        self.assertEqual(-2, skaiciu_suma(-2, -2, 2))
        self.assertEqual(15, skaiciu_suma(12, -2, 5))
        
     def test_saraso_suma(self):
        sarasas = [6, 0, 1, 5]
        sarasas_2 = [3, 5, 6, 8]
        sarasas_3 = []
        self.assertEqual(12, saraso_suma(sarasas)) 
        self.assertEqual(22, saraso_suma(sarasas_2))
        self.assertEqual(0, saraso_suma(sarasas_3))
        
     def test_didziausias_skaicius(self):
        self.assertEqual(76, didziausias_skaicius(45, 76, 43)) 
        self.assertEqual(132, didziausias_skaicius(23, 56, 99, 132))
        self.assertEqual(88, didziausias_skaicius(34, 67, 88, 23))
        
     def test_stringas_atbulai(self):
        stringas1 = "Kompiuteris"
        stringas2 = "Programa"
        stringas3 = "Maistas"
        self.assertEqual("siretuipmoK", stringas_atbulai(stringas1)) 
        self.assertEqual("amargorP", stringas_atbulai(stringas2))
        self.assertEqual("satsiaM", stringas_atbulai(stringas3))
        
     def test_info_apie_sakini(self):
        sakinys = "Kaip ilgai rasoma programa"
        sakinys2 = "2 kartus viskas"
        sakinys3 = "2022 Python Kursai"
        self.assertEqual(1, 22, 0 , info_apie_sakini(sakinys)) # rodo klaida
        self.assertEqual(0, 12, 1 , info_apie_sakini(sakinys2))
        self.assertEqual(2, 10, 4 , info_apie_sakini(sakinys3))
        
    


if __name__ == '__main__': # tikrina ar tikrai leidziama butent tas langas
    unittest.main() 