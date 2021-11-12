
# Ryan Monaghan
# I pledge my honor I have abided by the Stevens Honor System.
# class exercise using for-loop

def mapSqr(L):
    '''Assume L is a list of numbers; return map(sqr,L).
    Use a for-loop.'''
    modified = []
    for n in L:
        modified.append(n*n)
    return modified

def testMapSqr():
    assert mapSqr([1,2,3]) == list(map(lambda x: x*x, [1,2,3]))