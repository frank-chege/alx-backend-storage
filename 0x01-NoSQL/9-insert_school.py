#!/usr/bin/env python3
'''insert a doc into a collection'''
from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    '''insert a doc into a collection'''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id