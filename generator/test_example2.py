from example2 import adjrange

def test_normal_stepping():
    x = adjrange(0, 5, 1)
    assert list(x) == [0, 1, 2, 3, 4]

def test_adjusted_stepping():
    x = adjrange(0, 5, 1)
    assert next(x) == 0
    assert next(x) == 1
    # we do not care about the return value from .send()
    x.send(3)
    assert next(x) == 4
    # check that the generator is exhausted
    assert list(x) == []

def test_adjusted_stepping2():
    x = adjrange(0, 6, 1)
    assert next(x) == 0
    assert next(x) == 1
    x.send(3)
    x.send(2)
    assert next(x) == 3
    assert next(x) == 5
    assert list(x) == []
