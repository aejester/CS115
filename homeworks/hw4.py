#Name: Ryan Monaghan
#Pladge: I pledge my honor I have abided by the Stevens Honor System.

def calc_row(p):
    """Helper function for pascal row."""
    if len(p) ==0:
        return []
    elif len(p) == 1:
        return [1]
    return [p[0] + p[1]] + calc_row(p[1:])

#pascal_row
def pascal_row(n, curr_row=[1]):
    """Calculates the nth row of the pascal triangle."""
    if n == 0:
        return curr_row
    if curr_row == [1]:
        return pascal_row(n-1, [1, 1])
    else:
        curr_row = [1] + calc_row(curr_row)
        return pascal_row(n-1, curr_row)

#pascal_triangle
def pascal_triangle(n):
    """The pascal trignale function."""
    if n == 0:
        return [[1]]
    return pascal_triangle(n-1) + [pascal_row(n)]

#test_pascal_row
def test_pascal_row():
    """Test funciton for pascal_row."""
    assert pascal_row(1) == [1, 1]
    assert pascal_row(2) == [1, 2 ,1]
    assert pascal_row(0) == [1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]

#test_pascal_triangle
def test_pascal_triangle():
    """Test function for pascal_triangle."""
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
