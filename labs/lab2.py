#Name: Ryan Monaghan Jr.
#Pledge: I pledge my honor that I have abided by the stevens honor system.

def dot(l, k):
    """
    Finds the dot product of vectors of length len(l) (assuming len(l) == len(k)).
    """
    if len(l) != len(k):
        return "Lists are different lengths!"
    elif l == [] and  k == []:
        return 0.0
    else:
        return l[0]*k[0] + dot(l[1:], k[1:])

def explode(s):
    """
    Breaks string s up into a list.
    """
    if s == "":
        return []
    else:
        return [s[0:1]] + explode(s[1:])

def ind(e, l):
    """
    Returns the index at which element e appears in list l.
    """
    if len(l) == 0 or e == l[0]:
        return 0
    else:
        return 1 + ind(e, l[1:])

def removeAll(e, l):
    """
    Removes all top-level elements in a list l that matches e.
    """
    if l == []:
        return []
    elif e == l[0]:
        return removeAll(e, l[1:])
    else:
        return [l[0]] + removeAll(e, l[1:])

def myFilter(f, li):
    """
    Executes function f on list li, recursively.
    """
    if li == []:
        return []
    else:
        return [li[0]] + myFilter(f, li[1:]) if f(li[0]) == True else myFilter(f, li[1:])

def deepReverse(l):
    """
    Reverses nested list l.
    """
    if l == []:
        return list(reversed(l))
    elif isinstance(l[0], list):
        return deepReverse(l[1:]) + [deepReverse(l[0])] 
    else:
        return deepReverse(l[1:]) + [l[0]]