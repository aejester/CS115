# I pledge my honor I have abided by the Stevens Honor System.
# Ryan Monaghan

# Demo of hmmm, the Harvey Mudd miniature machine
# D.Naumann 2015, rev Oct 2018

# When this file is loaded, it runs the program assigned
# to variable RunThis. Debug mode is controlled by 
# variable Mode. Read all the comments before trying it out.
# Remember to press F5 to run, after making changes.  

import sys
import importlib
# Also requires hmmmAssembler.py and hmmmSimulator.py to
# be available in the same directory as this file.


# Example1 is an example program that
#   1) asks the user for two inputs
#   2) computes the product of the inputs
#   3) prints out the result (with write)
#   4) stops

Example1 = """
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 mul r3 r1 r2     # assign r3 = r1 * r2
03 write r3         # print what's in r3
04 halt             # stop.
"""


# Example2 is an example program that
#   1) asks the user for an input
#   2) counts up from that input
#   3) keeps going and going...

Example2 = """
00 read r1          # get # from user to r1
01 write r1         # print the value of r1
02 addn r1 1        # add 1 to r1
03 jumpn 01         # jump to line 01
04 halt             # never halts! [use ctrl-c]
"""

# AbsVal is a program that asks the user for
# an input and then prints its absolute value.

AbsVal = """
00 read r1
01 jltz r1 4     # if r1 < 0 go to line 4
02 write r1      # print the absolute value
03 halt
04 setn r2 -1
05 mul r1 r1 r2  # assign r1 = r1 * -1 
06 jumpn 2       # go to line 2  
"""

# StoreLoad is an example program that
#   1) asks the user for an input
#   2) stores the value in a memory location
#   3) increments it and stores in another location
#   4) loads from that location and writes that value
# Try changing 11 to the address of an instruction!

StoreLoad = """
00 read r1         
01 storen r1 11   # put the value into mem[11]
02 addn r1 1       
03 setn r2 13 
04 storer r1 r2   # put incremented value into mem[13]
05 loadn r1 13
06 write r1       # write what was loaded
07 halt
"""

Triangle1 = """
00 read  r1          # get base
01 read  r2          # get height
02 mul   r1 r1 r2    # b times h into r1
03 setn  r2 2
04 div   r1 r1 r2    # divide by 2
05 write r1
06 halt
"""

Factorial = """
# Input: n 
# Assume: n >= 0
# Output: n!
#

# register usage: r1 for the input, r13 for the output

0       read    r1         # Get n
1       setn    r13 1      # initialize r13
2       jeqzn   r1 6       # done if r1 is 0
3       mul     r13 r13 r1 # change r13 = r13 * r1
4       addn    r1 -1      # change r1 = r1 - 1
5       jumpn   2          # repeat
6       write   r13
7       halt
"""

Fibbonacci = """
00 read r1      #; reads number from user
01 jeqzn r1 19  #; prevents user input from being 0 (jump to line 19 whenever we want to end the program because r1 = 0)
02 setn r2 0    #; initializes r2 to hold the value of 0
03 setn r3 1    #; initializes r3 to hold the value of 1
04 write r2     #; prints out the initial value of r2 to the screen
05 addn r1 -1   #; subtract 1 from r1
06 jeqzn r1 19  #; r1 = 0, halt
07 write r3     #; prints out the initial value of r3 to the screen
08 addn r1 -1   #; subtract 1 from r1
09 jeqzn r1 19  #; r1 = 0, halt
10 add r2 r2 r3 #; takes the values of r2 and r3 and puts them into r2 (basically r2 += r3)
11 write r2     #; prints out the value of r2 to the screen
12 addn r1 -1   #; subtract 1 from r1
13 jeqzn r1 19  #; r1 = 0, halt
14 add r3 r2 r3 #; takes the values of r3 and r2 and puts them into r3 (basically r3 += r2)
15 write r3     #; prints out the value of r3 to the screen
16 addn r1 -1   #; subtract 1 from r1
17 jeqzn r1 19  #; r1 = 0, halt
18 jumpn 10     #; jumps to 10 if no previous conditions are met
19 halt         #; halts program
"""

ClassProblem = """
00 read r1
01 jltzn r1 08
02 setn r2 0
03 sub r3 r1 r2
04 write r2
05 addn r2 1
06 jeqzn r3 08 
07 jumpn 03
08 halt
"""

# Set this variable to whichever program you want to execute
# when this file is loaded.
RunThis = ClassProblem

# Choose whether to use debug mode; uncomment one of the following lines.
# Mode = ['-n'] # not debug mode, 
Mode = ['-n'] # debug mode
#Mode = []     # prompt for whether to enter debug mode


# When you press F5 in IDLE, the following code will
# load the assembler and simulator, then run them.
# You can interrupt with Ctrl-C; then re-start Python.

if __name__ == "__main__" : 
    import hmmmAssembler ; importlib.reload(hmmmAssembler)
    import hmmmSimulator ; importlib.reload(hmmmSimulator)
    hmmmAssembler.main(RunThis) # assemble input into machine code file out.b
    hmmmSimulator.main(Mode)    # run the machine code in out.b


