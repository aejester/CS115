# Name: Ryan Monaghan
# Pledge: I pledge my honor I have abided by the Stevens Honor System.

def knapsack(capacity, items):
    """
    Returns the amount of items that can fit in a knapsack based on weight and cost of the item.
    """
    if len(items) == 0 or capacity == 0:
        return [0, []]
    elif items[0][0] > capacity:
        return knapsack(capacity, items[1:])
    else:
        use_ = knapsack(capacity - items[0][0], items[1:])
        use = [use_[0] + items[0][1], [items[0]] + use_[1]]
        
        lose = knapsack(capacity, items[1:])
        
        return use if use[0] > lose[0] else lose

