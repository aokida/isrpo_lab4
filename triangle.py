import unittest
class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
        res = area(0, 5)
        self.assertEqual(res, 0)
    def test_area_negative(self):
        res = area(-5, 4)
        self.assertEqual(res, ValueError)
    def test_area_big_numbers(self):
        res = area(10000000000000000000, 100000000000000000000000)
        self.assertEqual(res, 5e+41)
        res = area(1312932929131.99092, 5677654556765456.110101)
        self.assertEqual(res, 3727189813906832952522758596.01042614146)
    def test_area_small_numbers(self):
        res = area(1, 1)
        self.assertEqual(res, 0.5)
        res = area(2.4, 1)
        self.assertEqual(res, 1.2)
        res = area(3.654, 2.19392)
        self.assertEqual(res, 4.00829184)

    def test_perimeter_zero(self):
        res = perimeter(0,0,0)
        self.assertEqual(res, 0)
        res = perimeter(0,5,3)
        self.assertEqual(res, 8)
    def test_perimeter_negative(self):
        res = perimeter(-1, -2, 0)
        self.assertEqual(res, ValueError)
    def test_perimeter_big_numbers(self):
        res = perimeter(100000000000000000000, 432341241241284328, 132567654345654345654)
        self.assertEqual(res, 232999995586895629982)
        res = perimeter(123102321831.44343, 1731237.321, 167876556787.80930)
        self.assertEqual(res, 290980609856.57373)
    def test_perimeter_small_number(self):
        res = perimeter(1, 4, 5)
        self.assertEqual(res, 10)
        res = perimeter(5.3, 2.0, 8.9)
        self.assertEqual(res, 16.2)

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
