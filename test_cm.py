#File for unit tests for cm.py

import pytest
import math
from cm import cMatrix
#argument order, sens, spec, [prevalence]

def test_known_case():
    m = cMatrix(0.9, 0.9, 0.1)
    assert math.isclose(m.ppv(), 0.5)
    assert math.isclose(m.npv(), 810 / 820)

def test_second_known_case():
    m = cMatrix(0.9, 0.8, 0.1)
    assert math.isclose(m.ppv(), 9/27)
    assert math.isclose(m.npv(), 72 / 73)


#check invalid input error:
def test_invalid_sens():
    with pytest.raises (ValueError):
        cMatrix(100,0.9, 0.1)

def test_invalid_spec():
    with pytest.raises (ValueError):
        cMatrix(0.9,90, 0.1)

def test_invalid_prev():
    with pytest.raises (ValueError):
        cMatrix(0.9,0.9, -0.1)

def test_invalid_population():
    with pytest.raises(ValueError):
        cMatrix (0.9, 0.9, 0.1, population = 0)

#Check for divide by 0 error 
def test_undefined_ppv():
    assert math.isnan(cMatrix(0.0, 1.0, 0.1).ppv())


def test_undefined_npv():
    assert math.isnan(cMatrix(1.0, 0.0, 0.1).npv())

#independent instances 
def test_instances_are_independent():
    a = cMatrix(0.9, 0.9, 0.1)
    b = cMatrix(0.8, 0.7, 0.3)
    assert a.ppv() == pytest.approx(0.5)
    assert b.ppv() != pytest.approx(a.ppv())


def test_population_size_does_not_change_result():
    small = cMatrix(0.9, 0.9, 0.1, population=100)
    large = cMatrix(0.9, 0.9, 0.1, population=100_000)
    assert small.ppv() == pytest.approx(large.ppv())
    assert small.npv() == pytest.approx(large.npv())