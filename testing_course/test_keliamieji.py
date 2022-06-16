# import unittest
# from keliamieji import ar_keliamieji

# class TestKeliamieji(unittest.TestCase):

#     def test_ar_keliamieji_2000(self):
#         rezultatas = ar_keliamieji(2000)
#         lukestis = "Keliamieji"
#         self.assertEqual(lukestis, rezultatas)
        
#     def test_ar_keliamieji_2100(self):
#         rezultatas = ar_keliamieji(2100)
#         lukestis = "Nekeliamieji"
#         self.assertEqual(lukestis, rezultatas)
        
#     if __name__ == '__main__':
#         unittest.main()


import unittest
from keliamieji import ar_keliamieji

class TestKeliamieji(unittest.TestCase):
    def test_ar_keliamieji(self):
        self.assertEqual("Keliamieji", ar_keliamieji(2000))
        self.assertEqual("Keliamieji", ar_keliamieji(2020))
        self.assertEqual("Keliamieji", ar_keliamieji(2100))


if __name__ == '__main__':
    unittest.main()