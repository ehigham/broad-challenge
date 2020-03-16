# -*- coding: utf-8 -*-
"""Functional utilities"""
#pylint: disable=invalid-name

def fmap(f, xs):
    """
    Map a function f over the values in an iterable xs and return a list
    This in effect is the same function as `map`, only returning a list for
    convenience
    """
    return list(map(f, xs))

def compose(f, g):
    """
    Return a function that applies g to its argument and then f
    """
    return lambda x: f(g(x))

def length(xs):
    """Return the number of elements in the list"""
    return len(xs)

def head(lst):
    """
    Get the first item in a list
    Example:
        assert first([1,2,3]) == 1
    """
    return lst[0]

def tail(lst):
    """
    Return the list without the first item
    Example:
        assert tail([1, 2, 3]) == [2, 3]
    """
    return lst[1:]

def last(lst):
    """
    Get the last element in a list
    Example:
        assert last([1,2,3]) == 3
    """
    return lst[-1]

def fst(pair):
    """Return the first item in a pair"""
    return pair[0]

def snd(pair):
    """Return the second item in a pair"""
    return pair[1]

def zip_with(f, xs, ys):
    """
    Generalization of zip where the function f is applied
    instead of making a tuple.
    """
    return [f(a, b) for (a, b) in zip(xs, ys)]

def flatten(xs):
    """Convert a list of iterables into a flat list"""
    return [y for ys in xs for y in ys]

def on(f, g):
    """
    Return a binary function that applies unary function g to its
    arguments, then calls binary function f with those values:
        on(f, g) = \\x, y -> f(g(x), g(y))
    """
    # pylint: disable=invalid-name
    return lambda x, y: f(g(x), g(y))
