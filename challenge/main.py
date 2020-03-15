# -*- coding: utf-8 -*-

from argparse import (Action, ArgumentParser)

from .functional import (foreach, compose, length, sort, head, last)
from .routes import (load_routes, route_long_name, num_stops)

def __print_route_info(route):
    spec = "{name}, {n:d} stops"
    print(spec.format(name=route_long_name(route), n=num_stops(route)))

def __decode_selector(name):
    return last if name == "longest" else head

def list_routes():
    """Question 1: List the long names of all routes"""
    for name in map(route_long_name, load_routes()):
        print(name)

def print_route(selector):
    """
    Print the name of the route supplied by the selector, along with the number
    of stops
    """
    routes = sort(num_stops, load_routes())
    __print_route_info(selector(routes))

def main():
    """Entry point"""
    parser = ArgumentParser(description='Broad Institute Coding Challenge')
    parser.add_argument('-l',
                        '--list-routes',
                        dest='list_routes',
                        action='store_true',
                        help='list all "Light" and "Heavy Rail" subway routes')
    parser.add_argument('-p',
                        '--print-route',
                        dest="route_type",
                        choices=['longest', 'shortest'],
                        help='print the longest route and its number of stops')

    args = parser.parse_args()
    if args.list_routes:
        list_routes()
    elif args.route_type:
        print_route(__decode_selector(args.route_type))
    else:
        parser.print_usage()


if __name__ == "__main__":
    main()
