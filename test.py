#!/usr/bin/python3

import unittest

from unittest.main import main
from max import max

class TestMax(unittest.TestCase):
    def test_max_1(self):
        self.assertEqual(max([4,3,1,2,5,7,6]),7)

    def test_max_2(self):
        self.assertEqual(max([1,2]),2)

    def test_max_3(self):
        self.assertEqual(max([1],1)

if  __name__ == '__main__':
    unittest.main()                         
