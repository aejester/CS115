###########################################################################
# RULES: You can use the following:
# Canvas to download+upload the exam
# IDLE to edit this file and check your solutions
# Blank paper if you find that helpful work working on your solutions  
# No other resources other than your mind.  
# You have 15 minutes
#
# Hint: If some of your code doesn't work, comment it out and write a note
# so your file still runs.
# 
# Name and pledge:
# Ryan Monaghan
# I pledge my honor I have abided by the Stevens Honor System.
#
#
#
###########################################################################
###########################################################################
# Question 0
# Write a function called tail_rev that given a list,
# returns its reverse using tail recursion
###########################################################################

def tail_rev(lst):
    if lst == []:
        return []
    return [lst[-1]] + tail_rev(lst[:-1])

def test_tailRev():
    assert tail_rev([1,2,3,4]) == [4,3,2,1]
    assert tail_rev([]) == []
    assert tail_rev(["tail", "recursion"]) == ["recursion", "tail"]