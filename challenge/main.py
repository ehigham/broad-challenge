# -*- coding: utf-8 -*-

from argparse import (ArgumentParser)
from .functional import (sort, head, last, length, fst, snd)
from .routes import (load_routes, get_stops, route_long_name, num_stops)
from .stops import (stop_name)

def __print_route_info(route):
    spec = "{name}, {n:d} stops"
    print(spec.format(name=route_long_name(route), n=num_stops(route)))

def __print_connection_info(stop, routes):
    spec = "{name}, {routes}"
    print(spec.format(name=stop, routes=routes))

def list_routes():
    """Question 1: List the long names of all routes"""
    for name in sort(str.lower, map(route_long_name, load_routes())):
        print(name)

def print_route(descriptor):
    """
    Print the name of the route described by descriptor, along with the number
    of stops. Valid descriptor are "longest" or "shortest"
    """
    routes = sort(num_stops, load_routes())
    selector = last if descriptor == "longest" else head
    __print_route_info(selector(routes))

def print_connections():
    """
    Print all stops that connect two or more routes along with the relevant
    route names for each of 'those stops'
    """
    stops = {}
    for route in sort(route_long_name, load_routes()):
        for stop in map(stop_name, get_stops(route)):
            if stop not in stops:
                stops[stop] = []
            stops[stop].append(route_long_name(route))

    connections = filter(lambda p: length(snd(p)) > 1, stops.items())
    for (stop, routes) in sort(lambda p: str.lower(fst(p)), connections):
        __print_connection_info(stop, routes)

def main():
    """Entry point"""
    parser = ArgumentParser(description='Broad Institute Coding Challenge')
    parser.add_argument('--list-routes',
                        dest='list',
                        action='store_true',
                        help='list all "Light" and "Heavy Rail" subway routes')
    parser.add_argument('--print-route',
                        dest="route_type",
                        choices=['longest', 'shortest'],
                        help='print the longest route and its number of stops')
    parser.add_argument('--print-connections',
                        dest="connections",
                        action='store_true',
                        help='print all stops that connect two or more routes ' +
                        'along with the relevant route names for each of ' +
                        'those stops')

    args = parser.parse_args()
    if args.list:
        list_routes()
    elif args.route_type:
        print_route(args.route_type)
    elif args.connections:
        print_connections()
    else:
        parser.print_usage()

if __name__ == "__main__":
    main()
