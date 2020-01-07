#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import unittest
from ossdev import Vector, Matrix


class VectorTest(unittest.TestCase):
    """Simple vector tests"""

    def __init__(self, *args, **kwargs):
        super(VectorTest, self).__init__(*args, **kwargs)

    def test_add(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a + b

        self.assertEqual(c.get(), [3, 3, 3, 3])

    def test_dot(self):
        a = Vector([1, 2])
        b = Vector([2, -1])
        self.assertEqual(a.dot(b), 0)

    def test_length(self):
        self.assertAlmostEqual(Vector([2, 4]).length(), 4.47213595499, 3)
        self.assertAlmostEqual(Vector([2, 4, 5]).length(), 6.708203932499369, 3)

        a = Vector([3, 4])
        self.assertEqual(a.length(), 5)

    def test_setitem(self):
        a = Vector(size = 4)
        a[1] = 1

        self.assertEqual(a[1], 1)

    def test_neg(self):
        a = Vector([1, 2, 3])
        b = -a

        self.assertEqual(b.get(), [-1, -2, -3])

    def test_reversed(self):
        a = Vector([1, 2, 3])
        b = reversed(a)
        self.assertEqual(b.get(), [3, 2, 1])

    def test_sub(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a - b

        self.assertEqual(c.get(), [-3, -1, 1, 3])

    def test_mul(self):
        a = Vector([-1, 0, 2])
        b = a * (-3)
        c = Vector([1, 2, 3])
        ac = a * c
        tc = c.transpose()
        ac_dot = tc * a
        ac_matrix = a * tc

        self.assertEqual(b.get(), [3, 0, -6])
        self.assertEqual(ac.get(), [-1, 0, 6])
        self.assertEqual(ac_dot, 5)
        self.assertIsInstance(ac_matrix, Matrix)
        
    def test_xor(self):
        a = Vector([-1, 0, 2])
        a3 = a ^ 3
        a3_result = [(-1)^3, 0^3, 2^3]

        b = Vector([0, 1, 0])
        ab = a ^ b
        ab_result = [0^(-1), 1^0, 2^0] 

        self.assertEqual(a3.get(), a3_result)
        self.assertEqual(ab.get(),  ab_result)

    def test_and(self):
        a = Vector([-1, 0, 2])
        a3 = a & 3
        a3_result = [(-1)&3, 0&3, 2&3]

        b = Vector([0, 1, 0])
        ab = a & b
        ab_result = [0&(-1), 1&0, 2&0] 

        self.assertEqual(a3.get(), a3_result)
        self.assertEqual(ab.get(),  ab_result)
        
    def test_cmp(self):
        a = Vector([3, 4])
        b = Vector([4, 3])
        c = Vector([0, 1])
        
        self.assertTrue(a == a)
        self.assertTrue(a == b)
        self.assertFalse(a == c)
        self.assertTrue(a > c)
        self.assertTrue(a >= c)
        self.assertFalse(b <= c)
        self.assertFalse(b < c)

    def test_dot(self):
        a = Vector([-1, 3, 4])
        b = Vector([1, 2, 3])
        ab = a.dot(b)
        ab_result = 17

        self.assertEqual(ab, ab_result)

    def test_transpose(self):
        a = Vector([0, 0, 0])
        a = a.transpose()

        self.assertTrue(a.row)

    def test_matrix_add(self):
        m = Matrix.square(2)
        e = Matrix.ident(2)

        m[0][0] = 5
        me = m + e

        self.assertEqual(me[0][0], 6)
        self.assertEqual(me[0][1], 0)
        self.assertEqual(me[1][0], 0)
        self.assertEqual(me[1][1], 1)

if __name__ == "__main__":
    unittest.main()  # pragma: no cover
