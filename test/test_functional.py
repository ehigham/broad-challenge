# -*- coding: utf-8 -*-

import challenge.functional as fn

import unittest

plus = lambda a, b: a + b
double = lambda a: a + a
square = lambda a: a * a

class TestFunctionalModule(unittest.TestCase):

    def test_fmap(self):
        self.assertListEqual(
            fn.fmap(square, [1, 2, 3]),
            [1, 4, 9])

        id_ = lambda x: x
        self.assertListEqual(
            fn.fmap(id_, [1, 2, 3]),
            [1, 2, 3])

    def test_compose(self):
        self.assertEqual(fn.compose(double, square)(5), 50)
        self.assertEqual(fn.compose(square, double)(5), 100)

    def test_length(self):
        self.assertEqual(fn.length([]), 0)
        self.assertEqual(fn.length([1, 2, 3]), 3)

    def test_head(self):
        with self.assertRaises(IndexError):
            fn.head([])

        self.assertEqual(fn.head([1, 2, 3]), 1)

    def test_tail(self):
        self.assertListEqual(fn.tail([]), [])
        self.assertListEqual(fn.tail([1, 2, 3]), [2, 3])

    def test_last(self):
        with self.assertRaises(IndexError):
            fn.last([])

        self.assertEqual(fn.last([1, 2, 3]), 3)

    def test_fst(self):
        self.assertEqual(fn.fst((1, 2)), 1)

    def test_snd(self):
        self.assertEqual(fn.snd((1, 2)), 2)

    def test_zip_with(self):
        res = fn.zip_with(plus, [1, 2, 3], [4, 5, 6])
        self.assertListEqual(res, [5, 7, 9])

    def test_on(self):
        res = fn.zip_with(fn.on(plus, double), [1, 2, 3], [4, 5, 6])
        self.assertListEqual(res, [10, 14, 18])

if __name__ == '__main__':
    unittest.main()