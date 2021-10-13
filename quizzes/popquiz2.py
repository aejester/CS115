# pop quiz Sept 17, 2021

# Ryan Monaghan
# I pledge my honor that I have abided by the Stevens Honor System.

def myMax(L, m=0):
    '''Assume L is a non-empty list of numbers.  Return the maximum value.'''
    if len(L) == 0:
        return m
    return myMax(L[1:], max(m, L[0]))