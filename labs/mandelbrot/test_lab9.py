from mandelbrot import *

def test():
    assert mult(6, 7) == 42
    assert mult(1.5, 28) == 42.0

    assert update(1, 3) == 5
    assert update(-1, 3) == -1
    assert update(1, 10) > 100
    assert update(-1, 10) == 0

    assert inMSet(0 + 0j, 25) == True
    assert inMSet(3 + 4j, 25) == False
    assert inMSet(0.3 + -0.5j, 25) == True
    assert inMSet(-0.7 + 0.3j, 25) == False
    assert inMSet(0.42 + 0.2j, 25) == True
    assert inMSet(0.42 + 0.2j, 50) == False

    assert scale(100, 200, -2.0, 1.0) == -0.5
    assert scale(100, 200, -1.5, 1.5) == 0.0
    assert scale(100, 300, -2.0, 1.0) == -1.0
    assert scale(25, 300, -2.0, 1.0) == -1.75
    assert scale(299, 300, -2.0, 1.0) >= 0.99 and scale(299, 300, -2.0, 1.0) < 1.0

    mset()

test()