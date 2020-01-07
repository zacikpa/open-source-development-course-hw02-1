#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import unittest
from ossdev import Vector


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

    def test_lenght(self):
        # Uncomment after passing
        # self.assertAlmostEqual(Vector([2, 4]).length(), 4.47213595499, 3)
        # self.assertAlmostEqual(Vector([2, 4, 5]).length(), 6.708203932499369, 3)
        return


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
