#########################################
# Name: Ryan Monaghan Jr.
# CS115 Homework 1
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#########################################


from functools import reduce

def factorial(n):
    """
    Returns the factorial of number n.
    """
    return reduce(lambda a, b: a * b, list(range(1, n+1)))

def mean(l):
    """
    Finds the average of list l.
    """
    return reduce(lambda a, b: a + b, l)/len(l)