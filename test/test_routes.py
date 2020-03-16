# -*- coding: utf-8 -*-

from challenge.functional import (length, fmap, fst, compose, head, last)
from challenge.main import (RouteChange, find_connecting_stops, make_itinerary)
from challenge.routes import (Stop, Route, load_routes, num_stops)

import unittest

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
        finish = Stop(2, 'b')
        middle = Stop(1, 'aa')
        routes = [Route(0, 'A', [start, middle]), Route(1, 'B', [middle, finish])]
        itin = make_itinerary(routes, start, finish)
        expected = [RouteChange(start, head(routes)),
                    RouteChange(middle, last(routes)),
                    RouteChange(finish, None)]

        self.assertListEqual(itin, expected)


if __name__ == '__main__':
    unittest.main()