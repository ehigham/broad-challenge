# -*- coding: utf-8 -*-

""" Defines the API for a stop """

def __get_attribute(stop, attr):
    return stop["attributes"][attr]

def stop_name(stop):
    """Get the name of this stop"""
    return __get_attribute(stop, "name")
