#!/usr/bin/env python3
'''insert a doc into a collection'''
from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    for doc in kwargs:
        mongo_collection.insert(doc)