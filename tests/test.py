import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import nfe

class NfeTests(unittest.TestCase):
    def test_nfe_instantiation(self):
        new_nfe = nfe.nf_e()
        self.assertIsNotNone(new_nfe)
