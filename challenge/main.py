# -*- coding: utf-8 -*-

from argparse import (Action, ArgumentParser)

from .functional import (foreach, compose)
from .routes import (load_routes, long_name)

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
