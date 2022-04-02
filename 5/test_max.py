import unittest

import max as my_max
class TestMax(unittest.TestCase):
    def test_max(self):
        self.assertEqual(32, my_max.max_(8, 5, 32))
        self.assertEqual(67, my_max.max_(5, 67, 66))
        self.assertEqual(100, my_max.max_(100, 100, 100))


if __name__ == '__main__':
    unittest.main()