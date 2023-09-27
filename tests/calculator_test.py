import pytest
from .calculator import Calculator  # Use a relative import

def test_add():
    calc = Calculator()
    result = calc.add(3, 4)
    assert result == 7


def test_subtract():
    calc = Calculator()
    result = calc.subtract(5, 2)
    assert result == 3


def test_multiply():
    calc = Calculator()
    result = calc.multiply(6, 7)
    assert result == 42


def test_divide():
    calc = Calculator()
    result = calc.divide(8, 4)
    assert result == 2.0


def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(8, 0)


def test_average():
    calc = Calculator()
    values = [1, 2, 3, 4, 5]
    result = calc.average(values)
    assert result == 3.0
