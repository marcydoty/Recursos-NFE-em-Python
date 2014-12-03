import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import nfe
from nfe.notafiscal import NotaFiscal

class NfeTests(unittest.TestCase):
    def test_nfe_instantiation(self):
        new_nfe = NotaFiscal()
        self.assertIsNotNone(new_nfe)
