# -*- coding: utf-8 -*-

from functools import (reduce)
from argparse import (Action, ArgumentParser)

from .routes import (load_routes, long_name)

def foreach(func, iterable):
    """Apply some function `func` on each item in an iterable"""
    for item in iterable:
        func(item)

def compose(*functions):
    """Compose two or more functions together"""
    return reduce(lambda f, g: lambda x: f(g(x)), functions, id)

def list_names():
    """Question 1: List the long names of all routes"""
    foreach(compose(print, long_name), load_routes())

def main():
    """Entry point"""
    parser = ArgumentParser(description="Broad Institute Coding Challenge")
    parser.add_argument('--list',
                        dest='execute',
                        action='store_const',
                        const=list_names,
                        help='list all "Light" and "Heavy Rail" subway routes')
    args = parser.parse_args()
    if args.execute:
        args.execute()
    else:
        parser.print_usage()

if __name__ == "__main__":
    main()
