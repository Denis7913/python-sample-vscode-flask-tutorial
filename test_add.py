def addition(x):
    return x + 1


def test_add_answer():
    assert addition(3) == 4
    assert addition(4) == 5

def test_wrong_add_answer():
    assert addition(6) != 6
