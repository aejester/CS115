#########################################
# Name: Ryan Monaghan Jr.
# CS115 Lab 1
#
# Pledge: I pledge my honor that I have abided by the stevens honor system.
#########################################

from math import factorial
from functools import reduce

def inverse(n):
    """
    Returns the reciprocal of number n.
    """
    return 1.0/n

def e(n):
    """
    Takes a number n and computes the value of e using a Taylor expansion.
    """
    return reduce(lambda a, b: a+b, map(lambda x: 1.0/factorial(x), list(range(n+1))))