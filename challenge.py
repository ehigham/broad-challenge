# -*- coding: utf-8 -*-

from argparse import (ArgumentParser)
from sys import (stderr)

from challenge.main import (list_routes, print_route, list_connections, plan_route)

def main():
    """Entry point to the Coding Challenge"""
    parser = ArgumentParser(description='Broad Institute Coding Challenge',
                            usage='challenge.py [options]')
    parser.add_argument('--list-routes',
                        dest='list_all_roots',
                        action='store_true',
                        help='list all "Light" and "Heavy Rail" subway routes')
    parser.add_argument('--print-route',
                        dest="route_type",
                        choices=['longest', 'shortest'],
                        help='print the longest route and its number of stops')
    parser.add_argument('--list-connections',
                        dest="list_all_connections",
                        action='store_true',
                        help='list all stops that connect two or more routes ' +
                        'along with the relevant route names for each of ' +
                        'those stops')
    parser.add_argument('--plan-route',
                        nargs=2,
                        metavar=('START', 'FINISH'),
                        dest='startfinish',
                        help='List the subway routes needed to travel from ' +
                        'the stop START to the stop FINISH.')

    args = parser.parse_args()
    if args.list_all_roots:
        list_routes()
    elif args.route_type:
        print_route(args.route_type)
    elif args.list_all_connections:
        list_connections()
    elif args.startfinish:
        plan_route(*args.startfinish)
    else:
        parser.print_usage()

if __name__ == "__main__":
    try:
        main()
    except ValueError as err:
        print(err, file=stderr)
