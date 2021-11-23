#!/usr/bin/python3

import unittest

from mymax import mymax

class TestMax(unittest.TestCase):
    def test_max_1(self):
        self.assertEqual(mymax([4,3,1,2,5,7,6]),7)

    def test_max_2(self):
        self.assertEqual(mymax([1,2]),2)
        
    def test_max_3(self):
        self.assertEqual(mymax([1,5,3]),5)
        
    def test_max_4(self):
        self.assertEqual(mymax([1,5,3,4]),4)

if __name__ == '__main__':
    unittest.main()
