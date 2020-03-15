# -*- coding: utf-8 -*-

"""Functional utilities"""

import functools

def identity(x):
    """
    The identity function - `identity` takes one argument and returns that
    argument unchanged.
    """
    return x

def foreach(func, iterable):
    """
    Apply a function `func` on each item in an iterable
    Example:
        foreach(print, [0, 1, 2, 3])
    """
    for item in iterable:
        func(item)

def foldl(func, state, iterable):
    """
    Apply a binary function to successive elements in an Iterable in
    left-to-right order.
    Example:
         sum = foldl(plus, 0, [1, 2, 3, 4])
    #    sum = ((((0 + 1) + 2) + 3) + 4)
    """
    for item in iterable:
        state = func(state, item)
    return state

def foldr(func, state, iterable):
    """
    Apply a binary function to successive elements in an Iterable in
    right-to-left order.
    Example:
         sum = foldr(plus, 0, [1, 2, 3, 4])
    #    sum = (1 + (2 + (3 + (4 + 0))))
    """
    return foldl(lambda a, b: func(b, a), state, iterable[::-1])

def compose(*functions):
    """
    Compose two or more functions together
    Example:
        h = compose(f, g)
    """
    return foldr(lambda f, g: lambda x: f(g(x)), identity, functions)
