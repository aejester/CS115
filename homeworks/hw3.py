'''
Created on 09/29/2021
@author:   Ryan Monaghan Jr.
Pledge:    I pledge my honor I have abided by the Stevens Honor System.

CS115 - Hw 3
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

def giveChange(amount, coins):
    '''
    Returns the amount of coins to add to a value and what they are.
    '''
    coins.sort()

    if amount == 0 or coins == [1]:
        return [amount, [1 for _ in range(amount)]]
    elif coins[-1] > amount:
        return giveChange(amount, coins[:-1])
    else:
        call = giveChange(amount - coins[-1], coins)
        use = [call[0] + 1, [coins[-1]] + call[1]]
        lose = giveChange(amount, coins[:-1])
        return use if use[0] < lose[0] else lose


# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2], ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1], ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1], ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo', 'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    final = []
    for word in dct:
        wordScore = 0
        for char in word:
            for _set in scores:
                if _set[0] == char:
                    wordScore += _set[1]
        final.append([word, wordScore])
    return final



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L, index = 0):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n == 0:
        return []
    elif index + 1 >= n:
        return [L[0]]
    return [L[0]] + take(n, L[1:], index + 1)



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L, index=0):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if index == 0:
        index = n
    
    if n == 0:
        return L
    elif index + 1 == len(L):
        return [L[index]]
    
    return [L[index]] + drop(n, L, index + 1)


