# Ryan Monaghan
# I pledge my honor I haveabided by the Stevens Honor System.

"""Kung Fu Panda has a number of staircases he needs to climb.
He likes to climb each staircase 1, 2, or 3 steps at a time.
Being a very precocious character, he wonders how many ways there are to reach
the top of the staircase. Your help is needed here. 
"""

"""
1. Write a recursive function KFP_slow that will take as an input a positive
integer denoting the number of stairs and will return the number of ways
Kung Fu Panda can climb those stairs.
"""
def KFP_slow(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return KFP_slow(n - 3) + KFP_slow(n - 2) + KFP_slow(n - 1)


print(KFP_slow(5))
print(KFP_slow(30))


"""
2. Use memoization to speed up your solution of KFP_slow.
"""
memo = {}
def KFP_fast(n):
    if str(n) in memo:
        return memo[str(n)]
    if n == 0 or n == 1:
        memo[str(n)] = 1
        return 1
    elif n == 2:
        memo[str(n)] = 2
        return 2
    else:
        ans = KFP_slow(n - 3) + KFP_slow(n - 2) + KFP_slow(n - 1)
        memo[str(n)] = ans
        return ans    
print(KFP_fast(5))
print(KFP_fast(30))


"""
3. Write a function called MeasureTime that takes as an input a function f and a integer n and returns the time needed for function f to finish runnig when given the input n
"""

import time
def MeasureTime(f, n):
    start_time = time.time()
    f(n)
    return time.time() - start_time

print("KFP slow takes: ", round(MeasureTime(KFP_slow, 30),2), "secs")
print("KFP fast takes: ", round(MeasureTime(KFP_fast, 30),6), "secs")

