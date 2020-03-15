# -*- coding: utf-8 -*-

"""Functional utilities"""

def identity(argument):
    """
    The identity function - `identity` takes one argument and returns that
    argument unchanged.
    """
    return argument

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
    chain = foldl(lambda g, a: lambda b: g(func(a, b)), identity, iterable)
    return chain(state)

def compose(*functions):
    """
    Compose two or more functions together
    Example:
        h = compose(f, g)
    """
    return foldr(lambda f, g: lambda x: f(g(x)), identity, functions)

def sort(comparator, iterable):
    """
    Sort the iterable with the specified comparator
    """
    return sorted(iterable, key=comparator)

def length(sequence):
    """Return the number of elements in the `sequence`"""
    return len(sequence)

def first(sequence):
    """Get the first element in a sequence"""
    return sequence[0]

def last(sequence):
    """Get the last element in a sequence"""
    return sequence[-1]
