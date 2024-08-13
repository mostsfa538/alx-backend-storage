#!/usr/bin/env python3
""" .... """
import pymongo


if __name__ == "__main__":
    """ ..... """
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
    total_status = col.count_documents({"method": "GET", "path": "/status"})
    print(f'{total_status} status check')

    print('IPs:')
    ips = [doc["ip"] for doc in col.find()]
    data = dict()
    for ip in ips:
        data[str(ip)] = 0
    for ip in ips:
        data[str(ip)] += 1

    sorted_data = dict(sorted(data.items(), key=lambda item: item[1],
                              reverse=True))
    i = 0
    for key, val in sorted_data.items():
        i += 1
        print(f'\t{key}: {val}')
        if i == 10:
            break
