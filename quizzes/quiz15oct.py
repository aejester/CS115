# Name: Ryan Monaghan
# Pledge: I plege my honor I have abided by the Stevens Honor System.

###Solve the following problems. Put the solutions as comments
# 1. What is the binary represantion of 37? 
# ANS Q1: 100101
# 2. What is the base 10 representation of 10101110?
# ANS Q2: 2 + 4 + 8 + 32 + 128 = 174 
# 3. What is the base 10 representation of 1.1011?
# ANS Q3: 1.6875
# 4. Assume that we have only 8 bits to represent numbers
#    apply two's compliment to represent -17.
# ANS Q4: 11101111
###


### Solve the following map/reduce/filter exercise
# You can use 'in', len, map, filter, and reduce, but try to solve it without
# using fancy Python library functions.

from functools import reduce

Vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

S = '''On this first Monday of October, students and adults alike
are encouraged to BlueUp by wearing our blue shirt or their own
to make that the day that bullying prevention is heard around the world
We chose blue because in many diverse cultures blue brings peace
'''

listOfWords = S.split()

def deVowel(w):
    """Assuming w is a word, remove its vowels.
    For example, deVowel('friday') is 'frdy'."""
    if w == "":
        return ""
    elif w[0] in Vowels:
        return deVowel(w[1:])
    return w[0] + deVowel(w[1:])

'''Now, change the expression in this assignment so it sets longest to
be one of the longest words in listOfWords, ignoring vowels.  One correct
answer is 'students'. '''
longest = reduce(lambda word1, word2: word1 if len(word1[1]) >= len(word2[1]) else word2, list(map(lambda word: [word, deVowel(word)], listOfWords)))[0]
                                                             
print(longest)




