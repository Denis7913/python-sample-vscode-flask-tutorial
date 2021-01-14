def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4
    assert func(4) == 5

def test_wrong_answer():
    assert func(6) != 8
    
