# -*- coding: utf-8 -*-

from networkx import (MultiGraph, shortest_path)
from .functional import (on, flatten, fmap, fst, head, last, length, snd, tail, zip_with)
from .routes import (Route, load_routes, num_stops)

def __print_route_info(route):
    spec = "{name}, {n:d} stops"
    print(spec.format(name=route.name(), n=num_stops(route)))

def __print_connection_info(stop, routes):
    spec = "{name}, {routes}"
    print(spec.format(name=stop, routes=routes))

def __make_stop_list(routes):
    stops = {}
    for route in sorted(routes, key=Route.name):
        for stop in route.stops():
            id_ = stop.id()
            if id_ not in stops:
                stops[id_] = (stop.name(), [])

            snd(stops[id_]).append(route.name())

    return list(stops.values())

def __find_connecting_stops(routes):
    stops = __make_stop_list(routes)
    return filter(lambda p: length(snd(p)) > 1, stops)

def __make_stop_dictionary(routes):
    stops = {}
    for route in routes:
        for stop in route.stops():
            name_ = stop.name().lower()
            if name_ not in stops:
                stops[name_] = {'ambiguous': False, 'stop': stop, 'routes': []}

            found = stops[name_]
            found["ambiguous"] = stop.id() != found["stop"].id()

    return stops

def __make_route_graph(routes):
    graph = MultiGraph()
    for route in routes:
        make_route_segment = lambda src, dst: (src, dst, {'route': route})
        segments = zip_with(make_route_segment, route.stops(), tail(route.stops()))
        graph.add_edges_from(segments)
    return graph

def __get_possible_route_segments(graph, path):
    # A segment is the pair (name, {routes}) where `name` is the name of
    # the start stop and `{routes}` is the set of all routes that could be
    # travelled via.
    edge_data = lambda a, b: graph.get_edge_data(a, b).values()
    get_route = lambda data: data["route"]
    make_route_set = lambda a, b: set(map(get_route, edge_data(a, b)))
    make_journey_segment = lambda a, b: (a, make_route_set(a, b))
    return zip_with(make_journey_segment, path, tail(path))

class RouteChange:
    """
    A Change represents a stop in the itinerary where a different route
    must be taken
    """
    def __init__(self, stop, route):
        self.__stop = stop
        self.__route = route

    def stop(self):
        """Get the stop at which this action should be performed"""
        return self.__stop

    def route(self):
        """Get the route onto which a passenger should change"""
        return self.__route

def __make_change(segment):
    return RouteChange(fst(segment), snd(segment).pop())

def __print_change(change):
    stop_name = change.stop().name()
    route_name = change.route().name() if change.route() else ""
    print("{stop} ({route})".format(stop=stop_name,
                                    route=route_name))

def __compute_itinerary(routes, start, finish):
    graph = __make_route_graph(routes)
    path = shortest_path(graph, start, finish)
    segments = __get_possible_route_segments(graph, path)

    current = __make_change(head(segments))
    itinerary = [current]
    for segment in tail(segments):
        if current.route() not in snd(segment):
            current = __make_change(segment)
            itinerary.append(current)

    itinerary.append(RouteChange(finish, None))
    return itinerary

def __on_unknown_stop(name):
    raise ValueError('Unknown stop "{name}"'.format(name=name))

def __on_ambiguous_stop(name):
    print('Warning: duplicate stop detected: "{name}"'.format(name=name.title()))
    print('Journey planner may be inaccurate')

def list_routes():
    """Question 1: List the long names of all routes"""
    for name in sorted(map(Route.name, load_routes())):
        print(name)

def print_route(descriptor):
    """
    Print the name of the route described by descriptor, along with the number
    of stops. Valid descriptor are "longest" or "shortest"
    """
    routes = sorted(load_routes(), key=num_stops)
    selector = last if descriptor == "longest" else head
    __print_route_info(selector(routes))

def list_connections():
    """
    Print all stops that connect two or more routes along with the relevant
    route names for each of 'those stops'
    """
    connections = __find_connecting_stops(load_routes())
    for (stop, routes) in sorted(connections, key=fst):
        __print_connection_info(stop, routes)

def plan_route(start, finish):
    """print the required routes to take to get from start to finish"""
    routes = load_routes()
    stop_names = __make_stop_dictionary(routes)
    for terminus in [start, finish]:
        if terminus.lower() not in stop_names:
            __on_unknown_stop(terminus)
        if stop_names[terminus.lower()]['ambiguous']:
            __on_ambiguous_stop(terminus)

    # use dijkstra to find the shortest path
    get_stop = lambda name: stop_names[name.lower()]['stop']
    itinerary = __compute_itinerary(routes, get_stop(start), get_stop(finish))
    for change in itinerary:
        __print_change(change)
