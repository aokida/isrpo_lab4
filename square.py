import unittest
class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)
        
    def test_area_negative(self):
        res = area(-10)
        self.assertEqual(res, ValueError)

    def test_area_big_numbers(self):
        res = area(100000000000)
        self.assertEqual(res, 10000000000000000000000)
        res = area(147128129010.3734)
        self.assertEqual(res, 21646686346093078866844.80742756)

    def test_area_small_numbers(self):
        res = area(5)
        self.assertEqual(res, 25)
        res = area(2.8)
        self.assertEqual(res, 7.84)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_negative(self):
        res = perimeter(-100)
        self.assertEqual(res, ValueError)

    def test_perimeter_big_numbers(self):
        res = perimeter(100000000000)
        self.assertEqual(res, 400000000000)
        res = perimeter(1032131231818178213.44348)
        self.assertEqual(res, 4128524927272712853.77392)

    def test_perimeter_small_numbers(self):
        res = perimeter(1)
        self.assertEqual(res, 4)
        res = perimeter(6.78)
        self.assertEqual(res, 27.12)


def area(a):
    '''
    Returns area of the square with side a
    Arguments: 
        a (int) - side of the square
    Return values:
        S (int) - area of the square
    '''
    return a * a


def perimeter(a):
    '''
    Returns perimeter of the square with side a
    Arguments: 
        a (int) - side of the square
    Return values:
        P (int) - perimeter of the square
    '''
    return 4 * a
