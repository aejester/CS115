'''
Created on 10/8/2021
@author:   Ryan Monaghan
Pledge:    I pledge my honor I have abided by the Stevens Honor System.

CS115 - Hw 5 
'''

lucas_memo = {}
change_memo = {}

def fast_lucas(n):
    if str(n) in lucas_memo:
        return lucas_memo[str(n)]
    elif n == 0:
        lucas_memo[str(n)] = 2
        return 2
    elif n == 1:
        lucas_memo[str(n)] = 1
        return 1
    else:
        ans = fast_lucas(n-1) + fast_lucas(n-2)
        lucas_memo[str(n)] = ans
        return ans

def fast_change(amount, coins):
    coins.sort()

    if (str(amount), str(coins)) in change_memo:
        return change_memo[(str(amount), str(coins))]

    if amount == 0:
        change_memo[(str(amount), str(coins))] = 0
        return 0
    elif amount > len(coins) and len(coins) == 0:
        change_memo[(str(amount), str(coins))] = float("inf")
        return float("inf")
    elif coins[len(coins) - 1] > amount:
        ans = fast_change(amount, coins[:-1])
        change_memo[(str(amount), str(coins))] = ans
        return ans
    else:
        use = 1 + fast_change(amount - coins[len(coins) - 1], coins)
        lose = fast_change(amount, coins[:-1])
        ans = min(use, lose)
        change_memo[(str(amount), str(coins))] = ans
        return ans

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


