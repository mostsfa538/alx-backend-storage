#!/usr/bin/env python3
""" .... """


def insert_school(mongo_collection, **kwargs):
    """ insert_school """
    x = mongo_collection.insert_one(kwargs)

    return (x.inserted_id)
