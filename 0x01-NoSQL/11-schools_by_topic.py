#!/usr/bin/env python3
'''find schools with a specific topic'''

from pymongo import MongoClient

def schools_by_topic(mongo_collection, topic):
    '''find schools with a specific topic'''
    result = mongo_collection.find({'topics': topic})
    return result