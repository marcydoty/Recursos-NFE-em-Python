import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nfe import NotaFiscalEletronica

class NfeTests(unittest.TestCase):
    def test_nfe_instantiation(self):
        new_nfe = NotaFiscalEletronica()
        self.assertIsNotNone(new_nfe)

if __name__ == "__main__":
    unittest.main()
