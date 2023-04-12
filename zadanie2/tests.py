import unittest
import calc

class testCase(unittest.TestCase):

    def test_L1(self):
        x = calc.getX(8, 39.413)
        result = calc.getL1(x,8.0)
        self.assertEqual(round(result,2),31.06)

    def test_L2(self):
        x = calc.getX(8, 39.413)
        result = calc.getL2(50, x, 10.0)
        self.assertEqual(round(result, 2), 130.66)

    def test_getTime(self):
        x = calc.getX(8, 39.413)
        L1 = calc.getL1(x, 8.0)
        L2 = calc.getL2(50, x, 10.0)
        result = calc.getAllTime(L1,L2,5,2)
        self.assertEqual(round(result, 1), 39.9)