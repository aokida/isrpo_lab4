import math
import unittest
class TestCircleCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_area_negative(self):
        try:
            res = area(-10)
        except ValueError:
            pass
        else:
            self.assertEqual(res, 0)

    def test_area_big_numbers(self):
        res = area(100000000000)
        self.assertEqual(res, 10000000000000000000000*math.pi)

    def test_area_small_numbers(self):
        res = area(5)
        self.assertEqual(res, 5*5*math.pi)
        res = area(2.5)
        self.assertEqual(res, 6.25*math.pi)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_negative(self):
        try:
            res = perimeter(-10)
        except ValueError:
            pass
        else:
            self.assertEqual(res, 0)

    def test_perimeter_big_numbers(self):
        res = perimeter(100000000000)
        self.assertEqual(res, 100000000000*2*math.pi)

    def test_perimeter_small_numbers(self):
        res = perimeter(5)
        self.assertEqual(res, 10*math.pi)
        res = perimeter(2.5)
        self.assertEqual(res, 5*math.pi)


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
