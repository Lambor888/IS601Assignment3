import pytest
from app.operations import addition, subtraction, multiplication, division


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_addition(a, b, expected):
    assert addition(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0),
])
def test_subtraction(a, b, expected):
    assert subtraction(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 1, -1),
    (0, 5, 0),
])
def test_multiplication(a, b, expected):
    assert multiplication(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (-6, 2, -3),
    (0, 5, 0),
])
def test_division(a, b, expected):
    assert division(a, b) == expected


def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        division(5, 0)
