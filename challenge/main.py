# -*- coding: utf-8 -*-

from networkx import (MultiGraph, shortest_path)
from .functional import (on, flatten, fmap, fst, head, last, length, snd, tail, zip_with)
from .routes import (Route, load_routes, num_stops)

def __print_route_info(route):
    spec = "{name}, {n:d} stops"
    print(spec.format(name=route.name(), n=num_stops(route)))

def __print_connection_info(stop, routes):
    spec = "{name}, {routes}"
    print(spec.format(name=stop, routes=fmap(Route.name, routes)))

def __make_stop_dictionary(routes):
    stops = {}
    for route in sorted(routes, key=Route.name):
        for stop in route.stops():
            name_ = stop.name().lower()
            if name_ not in stops:
                stops[name_] = {'stop': stop, 'routes': []}
            stops[name_]['routes'].append(route)
    return stops

def __make_route_graph(routes):
    graph = MultiGraph()
    for route in routes:
        make_route_segment = lambda src, dst: (src, dst, {'route': route.name()})
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

def __compute_itinerary(routes, start, finish):
    graph = __make_route_graph(routes)
    path = shortest_path(graph, start, finish)
    route_segments = __get_possible_route_segments(graph, path)

    # fixed-point of successive intersections of the sets of possible routes
    # At each point, we keep the start stop and take the intersection of the
    # sets of viable routes to propagate commonality.
    intersect = lambda a, b: (fst(b), on(set.intersection, snd)(a, b))
    while any(length(snd(s)) > 1 for s in route_segments):
        route_segments = zip_with(intersect, route_segments, tail(route_segments))

    return fmap(lambda x: (fst(x).name(), head(flatten([snd(x)]))), route_segments)

def __on_unknown_stop(name):
    raise ValueError('Unknown stop "{name}"'.format(name=name))

def __print_segment(segment):
    print("{stop} ({route})".format(stop=fst(segment),
                                    route=snd(segment)))

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
    stops = __make_stop_dictionary(load_routes())
    connections = filter(lambda entry: length(entry["routes"]) > 1, stops.values())
    connections = map(lambda x: (x["stop"].name(), x["routes"]), connections)
    for (stop, routes) in sorted(connections, key=fst):
        __print_connection_info(stop, routes)

def plan_route(start, finish):
    """print the required routes to take to get from start to finish"""
    routes = load_routes()
    stop_names = __make_stop_dictionary(routes)
    for terminus in [start, finish]:
        if terminus.lower() not in stop_names:
            __on_unknown_stop(terminus)

    # use dijkstra to find the shortest path
    get_stop = lambda name: stop_names[name.lower()]["stop"]
    route = __compute_itinerary(routes, get_stop(start), get_stop(finish))

    current = head(route)
    __print_segment(current)
    for segment in tail(route):
        if snd(segment) != snd(current):
            current = segment
            __print_segment(segment)

    __print_segment(last(route))
