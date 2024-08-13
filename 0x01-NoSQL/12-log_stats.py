#!/usr/bin/env python3
""" .... """
import pymongo


if __name__ == "__main__":
    """ main function """
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    col = db["nginx"]

    print(f'{col.count_documents({})} logs')
    print('Methods:')
    print(f'\tmethod GET: {col.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {col.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {col.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {col.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {col.count_documents({"method": "DELETE"})}')
    total_get_status = col.count_documents({"method": "GET", "path": "/status"})
    print(f'{total_get_status} status check')
