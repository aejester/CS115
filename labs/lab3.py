# Name: Ryan Monaghan
# Pledge: I pledge my honor I have abided by the Stevens Honor System.

def change(amount, coins):
    """
    Takes an amount where the amount > 0, and a list of coins (len(coins) >= 0) and returns the minimum number of coins to get to that amount.
    """
    coins.sort()

    if amount == 0:
        return 0
    elif amount > len(coins) and len(coins) == 0:
        return float("inf")
    elif coins[len(coins) - 1] > amount:
        return change(amount, coins[:-1])
    elif coins[len(coins) - 1] <= amount:
        return 1 + change(amount - coins[len(coins) - 1], coins)
    else:
        use = 1 + change(amount - coins[len(coins) - 1], coins)
        lose = change(amount, coins[:-1])
        return min(use, lose)

