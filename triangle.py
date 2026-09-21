def area(a, h): 
    '''
    Returns area of the triangle with side a and height h
    Arguments: 
        a (int) - one side of the triangle
        h (int) - height dropped to side a of the triangle
    Return values:
        S (int) - area of the triangle
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Returns perimeter of the triangle with sides a, b, c
    Arguments: 
        a (int) - first side of the triangle
        b (int) - second side of the triangle
        c (int) - third side of the triangle
    Return values:
        P (int) - perimeter of the triangle
    '''
    return a + b + c 
