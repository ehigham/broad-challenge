# -*- coding: utf-8 -*-

import unittest

from challenge.functional import (length, fmap, first, compose, last, tail)
from challenge.main import (find_connecting_stops,
                            make_itinerary, make_stop_lookup_table)
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
        stops = fmap(compose(Stop.name, first), connections)

        # Ambiguous stop name - occurs on two lines without connection
        self.assertNotIn('Saint Paul Street', stops)

    def test_longest_stortest_route(self):
        stops = sorted(self.routes, key=num_stops)
        most_stops = compose(Route.name, last)
        self.assertEqual(most_stops(stops), 'Green Line B')

        fewest_stops = compose(Route.name, first)
        self.assertEqual(fewest_stops(stops), 'Mattapan Trolley')

    def test_simple_plan_route(self):
        start = Stop(0, 'a')
        middle = Stop(1, 'b')
        finish = Stop(2, 'c')

        routes = [Route(0, 'A', [start, middle]), Route(1, 'B', [middle, finish])]
        itin = make_itinerary(routes, start, finish)
        expected = [(start, first(routes)),
                    (middle, last(routes)),
                    (finish, None)]

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
        expected = [(start, first(routes)),
                    (quarter, first(tail(routes))),
                    (half, first(tail(tail(routes)))),
                    (three_quarter, last(routes)),
                    (finish, None)]

        self.assertListEqual(itin, expected)

    def test_real_route(self):
        stops = make_stop_lookup_table(self.routes)
        start = stops['fenway']
        finish = stops['milton']
        itin = make_itinerary(self.routes, first(start), first(finish))

        itin = fmap(lambda x: (first(x).name(), last(x).name() if last(x) else ''), itin)
        self.assertListEqual(itin, [('Fenway', 'Green Line D'),
                                    ('Park Street', 'Red Line'),
                                    ('Ashmont', 'Mattapan Trolley'),
                                    ('Milton', '')])

if __name__ == '__main__':
    unittest.main()
