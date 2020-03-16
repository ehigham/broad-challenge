# -*- coding: utf-8 -*-

import unittest
from challenge.functional import (fmap, compose, length, first, tail, last, zip_with)

PLUS = lambda a, b: a + b
DOUBLE = lambda a: a + a
SQUARE = lambda a: a * a

class TestFunctionalModule(unittest.TestCase):

    def test_fmap(self):
        self.assertListEqual(
            fmap(SQUARE, [1, 2, 3]),
            [1, 4, 9])

        id_ = lambda x: x
        self.assertListEqual(
            fmap(id_, [1, 2, 3]),
            [1, 2, 3])

    def test_compose(self):
        self.assertEqual(compose(DOUBLE, SQUARE)(5), 50)
        self.assertEqual(compose(SQUARE, DOUBLE)(5), 100)

    def test_length(self):
        self.assertEqual(length([]), 0)
        self.assertEqual(length([1, 2, 3]), 3)

    def test_first(self):
        with self.assertRaises(StopIteration):
            first([])

        self.assertEqual(first([1, 2, 3]), 1)
        self.assertEqual(first((1, 2, 3)), 1)
        self.assertEqual(first(set([1, 2, 3])), 1)

    def test_tail(self):
        self.assertListEqual(tail([]), [])
        self.assertListEqual(tail([1, 2, 3]), [2, 3])

    def test_last(self):
        with self.assertRaises(IndexError):
            last([])

        self.assertEqual(last([1, 2, 3]), 3)
        self.assertEqual(last((1, 2, 3)), 3)

    def test_zip_with(self):
        res = zip_with(PLUS, [1, 2, 3], [4, 5, 6])
        self.assertListEqual(res, [5, 7, 9])

if __name__ == '__main__':
    unittest.main()
