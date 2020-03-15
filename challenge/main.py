# -*- coding: utf-8 -*-

from argparse import (Action, ArgumentParser)

from .functional import (foreach, compose, length, sort, first, last)
from .routes import (load_routes, long_name, get_stops)

def list_names():
    """Question 1: List the long names of all routes"""
    foreach(compose(print, long_name), load_routes())

def most_stops():
    """
    Question 2: The name of the subway route with the most stops as well as a
    count of its stops.
    """
    routes = sort(compose(length, get_stops), load_routes())
    compose(print, long_name, first)(routes)
    compose(print, long_name, last)(routes)

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
        most_stops()
    else:
        parser.print_usage()

if __name__ == "__main__":
    main()
