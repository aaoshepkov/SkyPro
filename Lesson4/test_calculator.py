import pytest
from calculator import Calculator

calc = Calculator()

@pytest.mark.parametrize('a, b, expected', [
    (5, 2, 7), 
    (1, 0, 1), 
    (128, 2, 130), 
    (-5, -2, -7), 
    (-10, 6, -4)
    ]
    )
def test_sum(a, b, expected):
    assert calc.sum(a, b) == expected

@pytest.mark.parametrize('a, b, expected', [
    (12, 4, 3),
    (22 , 2 , 11),
    (-12, 3, -4),
    (25, 5, 5),
    (100, 100, 1),
    ])
def test_div(a, b, expected):
    assert calc.div(a, b) == expected

@pytest.mark.parametrize('a, b', [
    (2, 0),
    (120, 0),
    (-2, 0)
    ]
    )
def test_zero_div(a, b):
    with pytest.raises(ArithmeticError, match="Нельзя делить на ноль"):
        calc.div(a, b)

@pytest.mark.parametrize('a, b, expected', [
    (2, 5, 10),
    (22 , 2 , 44),
    (-12, 1, -12),
    (25, 4, 100),
    (-100, 10, -1000)
    ])    
def test_mul(a, b, expected):
    assert calc.mul(a, b) == expected

@pytest.mark.parametrize('a, b, expected', [
    (20, 5, 15),
    (22 , 2 , 20),
    (-12, 1, -13),
    (25, 4, 21),
    (-100, -10, -90)
    ])
def test_sub(a, b, expected):
    assert calc.sub(a, b) == expected

def test_avg_empty():
    assert calc.avg([]) == 0


# --- ветка: обычные случаи ---
@pytest.mark.parametrize('arr, expected', [
    ([1], 1),                    # один элемент
    ([1, 2, 3], 2),              # целое среднее
    ([2, 4], 3),                 # целое среднее
    ([1, 2], 1.5),               # дробное среднее
    ([0, 0, 0], 0),              # нули
    ([-1, -2, -3], -2),          # отрицательные
    ([-5, 5], 0),                # сумма = 0
    ([10, 20, 30, 40], 25),
    ([1.5, 2.5], 2.0),           # float
])
def test_avg(arr, expected):
    assert calc.avg(arr) == expected