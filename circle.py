import math


def area(r):
    '''
    Returns area of the circle with radius r
    Arguments:
        r (int) - radius of the circle
    Return values:
        S (int) - area of the circle
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Returns perimeter of the circle with radius r
    Arguments: 
        r (int) - radius of the circle
    Return values:
        P (int) - perimeter of the circle
    '''
    return 2 * math.pi * r

