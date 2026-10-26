import unittest
from app import *
class DomainTests(unittest.TestCase):
    def test_donor_isolation(self):
        _,_,g=generate();tr,te=group_split(g,[6,7]);self.assertFalse(set(g[tr])&set(g[te]))
    def test_zero_library(self):self.assertTrue(np.isfinite(log_normalize(np.zeros((3,4)))).all())
    def test_library_normalization(self):np.testing.assert_allclose(log_normalize(np.array([[1.,2.],[2.,4.]]))[0],log_normalize(np.array([[1.,2.],[2.,4.]]))[1])
