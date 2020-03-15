# -*- coding: utf-8 -*-

import json
import requests

__URL = "https://api-v3.mbta.com/routes?filter[type]=0,1"
"""URL of the request"""

def _on_bad_response(response):
    raise RuntimeError("received " + str(response.status_code) + " from mbta")

def load_routes():
    """Query the mbta api for all type 0 and 1 routes"""
    #pylint: disable=no-member
    response = requests.get(__URL)
    if response.status_code != requests.codes.ok:
        _on_bad_response(response)

    payload = json.loads(response.text)
    return payload["data"]

def __get_attribute(route, attr):
    return route["attributes"][attr]

def long_name(route):
    """Get the `long_name` of a route"""
    return __get_attribute(route, "long_name")