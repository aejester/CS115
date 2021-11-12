# mandelbrot.py
# Lab 9
#
# I pledge my honor I have abided by the Stevens Honor System.
# Name: Ryan Monaghan

# keep this import line...
from cs5png import PNGImage

def mult(c, n):
    """Multiplies 2 numbers together without using multiplication."""
    result = 0
    for _ in range(n):
        result += c
    return result

def update(c, n):
    """Mandelbrot number calculator where the number of iterations to calculate is n"""
    z = 0
    for _ in range(n):
        z = z**2 + c
    return z

def inMSet(c, n):
    """Determines whether c is in the mandelbrot set up to n iterations."""
    z = 0
    for _ in range(n):
        if abs(z) > 2:
            return False
        z = z**2 + c
    return True

def scale(pix, pixMax, floatMin, floatMax):
    """returns the scale of pix on floatMin -> floatMax"""
    n = ((pix/pixMax) * (floatMax - floatMin)) + floatMin
    return n

def mset(): 
    """ creates a 300x200 image of the Mandelbrot set""" 
    width = 300 
    height = 200 
    image = PNGImage(width, height) 
 
    # create a loop in order to draw some pixels 
     
    for col in range(width): 
        for row in range(height): 
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            if inMSet(x + y*1j, 25) == True: 
                image.plotPoint(col, row) 
 
    # we looped through every image pixel; we now write the file 
 
    image.saveFile("mandelbrot_out.png")