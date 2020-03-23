#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import unittest
from ossdev import Vector

import math


class VectorTest(unittest.TestCase):
    """Simple vector tests"""

    def __init__(self, *args, **kwargs):
        super(VectorTest, self).__init__(*args, **kwargs)

    def test_cmp(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        self.assertEquals(a.__cmp__(b), -1)

    def test_reversed(self):
        a = reversed(Vector([1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(a.get(), [7, 6, 5, 4, 3, 2, 1])

    def test_add(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a + b

        self.assertEqual(c.get(), [3, 3, 3, 3])

    def test_setitem(self):
        a = Vector([1, 1, 1, 1, 1])
        a[2] = 0
        self.assertEqual(a.get(), [1, 1, 0, 1, 1])

    def test_sub(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([-3, -2, -1, -0])
        c = a - b

        self.assertEqual(c.get(), [3, 3, 3, 3])

    def test_mul(self):
        a = Vector([1, 2, 3, 4])
        b = 7

        self.assertEqual((a * b).get(), [7, 14, 21, 28])

    def test_xor(self):
        a = Vector([1, 2, 3])
        b = 2

        self.assertEqual((a ^ b).get(), [3, 0, 1])

    def test_length(self):
        a = Vector([3, 4])
        self.assertEqual(a.length(), 5)

        a = Vector([1, 2, 3, 4, 5])
        self.assertAlmostEqual(a.length(), math.sqrt(55))


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
