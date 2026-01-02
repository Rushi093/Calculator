import unittest
from mean_var_std import calculate

class TestMeanVarStd(unittest.TestCase):

    def test_calculate(self):
        result = calculate([0,1,2,3,4,5,6,7,8])

        self.assertEqual(result['mean'][0], [3.0, 4.0, 5.0])
        self.assertEqual(result['mean'][1], [1.0, 4.0, 7.0])
        self.assertEqual(result['mean'][2], 4.0)

        self.assertEqual(result['max'][2], 8)
        self.assertEqual(result['min'][2], 0)
        self.assertEqual(result['sum'][2], 36)

    def test_error(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3])
