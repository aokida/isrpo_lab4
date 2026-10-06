import unittest
import random
class TestRectangleCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        res = area(0, 0)
        self.assertEqual(res, 0)
       
    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_negative_int_numbers(self):
        try:
            res = area(-10, 10)
        except ValueError:
            pass
        else:
            self.assertEqual(res, 0)

    def test_area_big_int_numbers(self):
        res = area(100000000000, 100000000000)
        self.assertEqual(res, 10000000000000000000000)

    def test_area_random_positive_int_numbers(self):
        for i in range(10):
            a = random.randint(1, 10000000)
            b = random.randint(1, 10000000)
            res = area(a, b)
            self.assertEqual(res, a*b)

    def test_area_float_number(self):
        res = area(2.7182818284, 3.1415926535)
        self.assertEqual(res, 8.5397342222439876594)
        res = area(1.2, 3.0)
        self.assertEqual(res, 3.6)
        
    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
        res = perimeter(5, 0)
        self.assertEqual(res, 10)
           
    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_negative(self):
        try:
            res = area(-10, -10)
        except ValueError:
            pass
        else:
            self.assertEqual(res, 0)

    def test_perimeter_big_numbers(self):
        res = perimeter(100000000000, 100000000000)
        self.assertEqual(res, 400000000000)

    def test_perimeter_random_positive_int_numbers(self):
        for i in range(10):
            a = random.randint(1, 10000000)
            b = random.randint(1, 10000000)
            res = perimeter(a, b)
            self.assertEqual(res, (a+b)*2)

    def test_perimeter_float_number(self):
        res = perimeter(2.7182818284, 3.1415926535)
        self.assertEqual(res, 11.7197489638)
        res = perimeter(1.2, 3.0)
        self.assertEqual(res, 8.4)

    

def area(a, b): 
    '''
    Returns area of the rectangle with sides a and b
    Arguments: 
        a (int) - the first side of the rectangle
        b (int) - the second side of the rectangle
    Return values:
        S (int) - area of the rectangle
    '''
    return a * b 

def perimeter(a, b): 
    '''
    Returns perimeter of the rectangle with sides a and b
    Arguments: 
        a (int) - the first side of the rectangle
        b (int) - the second side of the rectangle
    Return values:
        P (int) - perimeter of the rectangle
    '''
    return 2*(a + b) 

