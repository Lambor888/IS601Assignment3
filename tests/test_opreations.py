from app.operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(0, 0) == 0
    assert subtraction(-1, -1) == 0

def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 5) == 0

def test_division():
    assert division(6, 3) == 2
    assert division(-6, 2) == -3
    try:
        division(5, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"