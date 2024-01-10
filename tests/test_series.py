from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci():
    assert fibonacci(2) == 1
    assert fibonacci(5) == 5
    assert fibonacci(7) == 13
    
def test_lucas():
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(8) == 47

def test_sum_fibonacci():
    assert sum_series(5) == fibonacci(5)
    assert sum_series(8) == fibonacci(8)

def test_sum_lucas():
    assert sum_series(5, 2, 1) == lucas(5)
    assert sum_series(6, 2, 1) == lucas(6)