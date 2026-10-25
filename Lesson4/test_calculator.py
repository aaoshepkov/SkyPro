import pytest
from calculator import Calculator

calc = Calculator()

@pytest.mark.parametrize('a, b, c', [
    (5, 2, 7), 
    (1, 0, 1), 
    (128, 2, 130), 
    (-5, -2, -7), 
    (-10, 6, -4)
    ]
    )
def test_sum(a, b, c):
    assert calc.sum(a, b) == c