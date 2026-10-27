#File for unit tests for cm.py

import math
from cm import cMatrix

def test_known_case():
    m = cMatrix(0.9, 0.9, 0.1)
    assert math.isclose(m.ppv(), 0.5)
    assert math.isclose(m.npv(), 810 / 820)

def test_undefined_ppv():
    assert math.isnan(cMatrix(0.0, 1.0, 0.1).ppv())