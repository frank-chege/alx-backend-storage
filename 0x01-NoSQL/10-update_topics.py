#!/usr/bin/env python3
'''update schoool topics'''
from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    '''update schoool topics'''
    mongo_collection.update_one(
        {'name': name},
        {'$set': {'topics': topics}}
    )