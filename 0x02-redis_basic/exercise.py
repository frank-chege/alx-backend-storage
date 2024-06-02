#!/usr/bin/env python3
'''redis basic'''
import redis
import uuid

class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data):
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key