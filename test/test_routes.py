# -*- coding: utf-8 -*-

import unittest

from challenge.functional import (length, fmap, fst, compose, head, last, tail)
from challenge.main import (RouteChange, find_connecting_stops,
                            make_itinerary, make_stop_dictionary)
from challenge.routes import (Stop, Route, load_routes, num_stops)

class TestRouteFinding(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.routes = load_routes()

    def test_load_routes(self):
        self.assertTrue(length(self.routes) > 1)

    def test_num_stops(self):
        for route in self.routes:
            self.assertTrue(num_stops(route) > 1)

    def test_connecting_stops(self):
        connections = find_connecting_stops(self.routes)
        stops = fmap(compose(Stop.name, fst), connections)

        # Ambiguous stop name - occurs on two lines without connection
        self.assertNotIn("Saint Paul Street", stops)

    def test_simple_plan_route(self):
        start = Stop(0, 'a')
        middle = Stop(1, 'b')
        finish = Stop(2, 'c')

        routes = [Route(0, 'A', [start, middle]), Route(1, 'B', [middle, finish])]
        itin = make_itinerary(routes, start, finish)
        expected = [RouteChange(start, head(routes)),
                    RouteChange(middle, last(routes)),
                    RouteChange(finish, None)]

        self.assertListEqual(itin, expected)


    def test_more_elaborate_plan_route(self):
        start = Stop(0, 'a')
        quarter = Stop(1, 'b')
        half = Stop(2, 'c')
        three_quarter = Stop(4, 'd')
        finish = Stop(3, 'e')
        routes = [Route(0, 'A', [start, Stop(-1, ''), Stop(-2, ''), quarter]),
                  Route(1, 'B', [quarter, Stop(-3, ''), half, Stop(-4, '')]),
                  Route(3, 'C', [Stop(-5, ''), half, three_quarter, Stop(-6, '')]),
                  Route(4, 'D', [Stop(-7, ''), three_quarter, Stop(-8, ''), finish])]
        itin = make_itinerary(routes, start, finish)
        expected = [RouteChange(start, head(routes)),
                    RouteChange(quarter, head(tail(routes))),
                    RouteChange(half, head(tail(tail(routes)))),
                    RouteChange(three_quarter, head(tail(tail(tail(routes))))),
                    RouteChange(finish, None)]

        self.assertListEqual(itin, expected)

    def test_real_route(self):
        stops = make_stop_dictionary(self.routes)
        start = stops["prudential"]["stop"]
        finish = stops["aquarium"]["stop"]
        itin = make_itinerary(self.routes, start, finish)

        stop_name = lambda c: c.stop().name()
        route_name = lambda c: c.route().name() if c.route() else ""

        itin = fmap(lambda change: (stop_name(change), route_name(change)), itin)
        self.assertListEqual(itin, [("Prudential", "Green Line E"),
                                    ("Park Street", "Red Line"),
                                    ("Downtown Crossing", "Orange Line"),
                                    ("State", "Blue Line"),
                                    ("Aquarium", "")])

if __name__ == '__main__':
    unittest.main()
