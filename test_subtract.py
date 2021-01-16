def subtract(x):
    return x - 1


def test_answer():
    assert subtract(3) == 2
    assert subtract(4) == 3

def test_wrong_answer():
    assert subtract(6) != 6
    
