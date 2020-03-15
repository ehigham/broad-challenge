# -*- coding: utf-8 -*-

""" Defines the API for a stop """

import json
import requests

from .functional import (length)

__URL = "https://api-v3.mbta.com"
"""URL of the request"""

def __on_bad_response(response):
    code = response.status_code
    detail = response.reason
    msg = "Received {code:d} from mbda: {detail}".format(code=code, detail=detail)
    raise RuntimeError(msg)

def __mbta_data_request(query):
    #pylint: disable=no-member
    response = requests.get(__URL + query)
    if response.status_code != requests.codes.ok:
        __on_bad_response(response)

    payload = json.loads(response.text)
    return payload["data"]

def __get_attribute(route, attr):
    return route["attributes"][attr]

def load_routes():
    """Query the mbta api for all type 0 and 1 routes"""
    return __mbta_data_request("/routes?filter[type]=0,1")

def route_long_name(route):
    """Get the `long_name` of a route"""
    return __get_attribute(route, "long_name")

def route_id(route):
    """Get the id of this route"""
    return route["id"]

def get_stops(route):
    """Get a list of stops on this route"""
    if "stops" in route:
        return route["stops"]

    stops = __mbta_data_request("/stops?filter[route]=%s" % route_id(route))
    route["stops"] = stops
    return stops

def num_stops(route):
    """Get the number of stops in the route"""
    return length(get_stops(route))
