#
# life.py - Game of Life lab
#
# Name: Ryan Monaghan
# Pledge: I pledge my honor I have abided by the Stevens Honor System.
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """Creates a 2d array with a given width and height."""
    return [createOneRow(width) for _ in range(height)]

def printBoard(board):
    """Prints the given 2d array."""
    for row in board:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write("\n")

def diagonalize(width,height): 
    """ creates an empty board and then modifies it 
        so that it has a diagonal strip of "on" cells. 
    """ 
    A = createBoard( width, height ) 
     
    for row in range(height): 
        for col in range(width): 
            if row == col: 
                A[row][col] = 1 
            else: 
                A[row][col] = 0      
 
    return A

def randomCells(w, h):
    """Generates a 2D array with a given width and height, does not touch outer borders."""
    L = []
    for i in range(h):
        R = []
        for j in range(w):
            if i != 0 and i != h - 1 and j != 0 and j != w:
                R += [random.choice([0, 1])]
            else:
                R += [0]
        L += [R]
    return L

def copy(L):
    """Copies list L and creates a new one."""
    newL = []
    for row in L:
        newR = []
        for col in row:
            newR += [col]
        newL += [newR]
    return newL

def innerReverse(L):
    """Swaps the 0s for 1s and the 1s for 0s in the inner cells."""
    C = copy(L)
    for i in range(len(L)):
        for j in range(len(L[i])):
            if i != 0 and i != len(L) - 1 and j != 0 and j != len(L[i]) - 1:
                C[i][j] = int(not L[i][j])
    return C

def next_life_generation(oldG):
    """Returns the next generation of life given the old generation's board."""
    newG = copy(oldG)

    for i in range(1, len(oldG) - 1):
        for j in range(1, len(oldG[0]) - 1):
            count = checkNeighbors(i, j, oldG)

            if count > 3:
                newG[i][j] = 0
            elif count == 3:
                newG[i][j] = 1
            elif count < 2:
                newG[i][j] = 0
    return newG

def checkNeighbors(r, c, G):
    """Checks the cells surrounding G[r][c]"""
    slopes = [(-1, -1), (-1, 0), (-1, 1),  (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]

    count = 0

    left_bound = 0
    right_bound = len(G[0]) - 1
    lower_bound = 0
    upper_bound = len(G) - 1

    for slope in slopes:
        if left_bound <= r + slope[0] <= right_bound and lower_bound <= c + slope[1] <= upper_bound:
            if G[r + slope[0]][c + slope[1]] == 1:
                count += 1
    return count