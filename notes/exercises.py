from functools import reduce
import math

def addTwoDigits(n):
    return int(n/10) + (n % 10)

def largestNumber(n):
    return 10**n-1

def reverse(l):
    return list(reversed(l))

def headtail(n):
    l = list(range(1, n+1))
    squares = list(map(lambda n: n**2, l))
    return squares[0:5] + squares[len(squares)-5:len(squares)]

def longestString(l):
    return reduce(lambda a, b: a if len(a) >= len(b) else b, l)

def inverseSquaresSum(n):
    l = list(range(1, n+1, 2))
    m = list(map(lambda x: 1/math.sqrt(x), l))
    return reduce(lambda a, b: a + b, m)

print(addTwoDigits(29))
print(largestNumber(2))
print(reverse([1, 2, 3, 4]))
print(headtail(20))
print(longestString(['introduction','to','CS','using','Python']))
print(inverseSquaresSum(5))