import unittest
from keliamieji2 import ar_keliamieji2

class TestKeliamieji(unittest.TestCase):
    def test_ar_keliamieji(self):
        self.assertTrue(ar_keliamieji2(2000))
        self.assertTrue(ar_keliamieji2(2020))
        self.assertFalsecd(ar_keliamieji2(2100))
        
if __name__ == '__main__': # tikrina ar tikrai leidziama butent tas langas
    unittest.main()