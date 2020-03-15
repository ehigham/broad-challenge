# -*- coding: utf-8 -*-

import json
import requests

__URL = "https://api-v3.mbta.com"
"""URL of the request"""

def __on_bad_response(response):
    raise RuntimeError("received " + str(response.status_code) + " from mbta")

def __mbta_data_request(query):
    """Send a request to the mbta api"""
    #pylint: disable=no-member
    response = requests.get(__URL + query)
    if response.status_code != requests.codes.ok:
        __on_bad_response(response)

    payload = json.loads(response.text)
    return payload["data"]

def load_routes():
    """Query the mbta api for all type 0 and 1 routes"""
    return __mbta_data_request("/routes?filter[type]=0,1")

def __get_attribute(route, attr):
    return route["attributes"][attr]

def long_name(route):
    """Get the `long_name` of a route"""
    return __get_attribute(route, "long_name")

def get_id(route):
    """Get the id of this route"""
    return route["id"]

def get_stops(route):
    """Get the number of stops on this route"""
    return __mbta_data_request("/stops?filter[route]=%s" % get_id(route))