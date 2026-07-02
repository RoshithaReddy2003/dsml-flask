from app import sum_something, sub_something, mul_something

def test_sum_something():
    a, b = 1, 3

    assert sum_something(a, b) == 4 


def test_sub_something():
    a, b = 5, 2

    assert sub_something(a, b) == 3

def test_mul_something():
    a, b = 2, 3

    assert mul_something(a, b) == 6
