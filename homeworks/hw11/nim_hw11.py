# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Ryan Monaghan
# I pledge my honor I have abided by the Stevens Honor System.

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            print("User won!")

            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

            print("Computer won!")

            break

def recieve_valid_int_input(f, text="Enter an integer: "):
    """Gets integer input from the user and only returns once it conforms to f where f is a function that returns a boolean"""
    try:
        integer = int(input(text))
    except ValueError:
        print("Invalid value.")
        integer = -1
    
    while not f(integer):
        try:
            integer = int(input(text))
        except ValueError:
            print("Invalid value.")
            integer = -1
    return integer

def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    
    _piles = recieve_valid_int_input(lambda n: n > 1, "How many piles do you want to play with? ")

    for pile in range(_piles):
        how_many = recieve_valid_int_input(lambda n: n > 1, "How many in pile "+str(pile)+"? ")
        piles += [how_many]
    
    num_piles = len(piles)
        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles

    for pile in range(num_piles):
        print("pile "+str(pile)+" = "+str(piles[pile]))


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles

    pile_choice = recieve_valid_int_input(lambda n: 0 <= n < num_piles, "Which pile? ")

    return pile_choice



def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    
    number_choice = recieve_valid_int_input(lambda n: 1 <= n <= piles[pnum], "How many? ")

    return number_choice


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles 

    summation = piles[0]

    for i in range(1, num_piles):
        summation ^= piles[i]

    return summation

def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles 

    nim_sum = game_nim_sum()

    pile_sums = [pile ^ nim_sum for pile in piles]

    for i in range(num_piles):
        if pile_sums[i] < piles[i]:
            return (i, piles[i] - pile_sums[i])
    
    for i in range(len(piles)):
        if piles[i] > 0:
            return (i, 1)


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles

    optimal_play = opt_play()
    piles[optimal_play[0]] -= optimal_play[1]
    print("Computer removed "+str(optimal_play[1])+" from pile "+str(optimal_play[0])+".")

    


#   start playing automatically
if __name__ == "__main__" : play_nim()
