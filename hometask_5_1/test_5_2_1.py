from my_5_2_1 import my_range

def test_my_range():
    assert my_range(start = 10, stop = 15, step = 2)
    assert my_range(15, step = 3)

def test_not_my_range():
    assert not my_range(start = 10, stop = 1, step = -1)
    assert not my_range(start = 10, stop = 5)
