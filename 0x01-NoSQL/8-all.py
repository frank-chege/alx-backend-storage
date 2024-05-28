#!/usr/bin/env python3
'''list docs in collection'''
from pymongo import MongoClient

def list_all(mongo_collection):
    '''list docs in collection'''
    result = mongo_collection.find()
    return list(result)