import pytest
from factorial import factorial
def test_fac0():
    assert factorial(0)==1
def test_fac5():
    assert factorial(5)==120
def test_fac4():
    assert factorial(4)==24