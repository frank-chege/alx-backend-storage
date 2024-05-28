#!/usr/bin/env python3
'''list docs in collection'''
from pymongo import MongoClient

def list_all(mongo_collection):
    '''list docs in collection'''
    client = MongoClient('localhost', 27017)
    db = client['my_db']
    result = db.mongo_collection.find()
    if result is None:
        return result
    else:
        for doc in result:
            yield doc