#!/usr/bin/env python3
""" .... """


def list_all(mongo_collection):
    """ list all """
    if mongo_collection is None:
        return []

    return mongo_collection.find()
