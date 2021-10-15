'''
Created on 10/14/2021
@author:   Ryan Monaghan
Pledge:    I pledge my honor I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
################################################
# Question 1: base 2 representation of 42 is 101010
################################################
# Question 2: if decimal is even, digit is 0, else 1
################################################
# Question 3 can be answered simply by:
#
# base10: 8 | 4 | 2 | 1 |
# base2 : 1 | 0 | 1 | 1 |
# = (1 * 1) + (2 * 1) + (4 * 0) + (8 * 1) = 11
#
# ----(remove trailing 1)----
#
# base10: 8 | 4 | 2 | 1 |
# base2 :   | 1 | 0 | 1 |
# = (1 * 1) + (2 * 0) + (4 * 1)           = 5
#
# Removing a digit from a binary string drastically changes the number because of the way that conversion from base n to base 10 works.
################################################
# Question 4: Let decimal = 10
# 1. if decimal is even, add 0, else 1, then
# 2. decimal //= 2
# repeat until there are infinite leading zeroes
################################################
# Question 5: 59 in ternary is 2012
# 2 * (3**3) + 0 * (3**2) + 1 * (3**1) + 2 * (3**0) = 59
################################################

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return not n % 2 == 0

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""

    return numToBinary(n//2) + str(n % 2)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if len(s) == 0:
        return 0
    
    return (int(s[0]) * (2**(len(s)-1))) + binaryToNum(s[1:])    

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if len(s) == 0:
        return ""
    elif s[-1] == "0":
        return s[:-1] + "1"
    else:
        return increment(s[:-1]) + "0"

def count(s, n, accum=0):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        print(s)
        return
    if accum == 0:
        print(s)
        return count(s, n, accum+1)
    elif accum == n:
        print(increment(s))
        return
    else:
        x = increment(s)
        print(x)
        return count(x, n, accum+1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ""

    return numToTernary(n//3) + str(n % 3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''

    if len(s) == 0:
        return 0
    
    return (int(s[0]) * (3**(len(s)-1))) + ternaryToNum(s[1:])

def decimalToBaseN(n, base):
    '''Converts a num to a num in the specified base.'''
    if n == 0:
        return ""

    return decimalToBaseN(n//base) + str(n % base)

def baseNtoDecimal(s, base):
    '''Converts a base n number to a num in decimals.'''
    if len(s) == 0:
        return 0
    
    return (int(s[0]) * (base**(len(s)-1))) + baseNtoDecimal(s[1:])