from hw7 import *

def test():
    assert findRunBits(L0) == 2
    assert findRunBits(L1) == 1
    assert findRunBits(L2) == 2
    assert findRunBits(L3) == 2
    assert findRunBits(L4) == 3
    assert findRunBits(L5) == 3
    assert findRunBits(L6) == 6
    assert findRunBits(L7) == 5
    assert findRunBits(L8) == 6

test()