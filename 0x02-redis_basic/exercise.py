#!/usr/bin/env python3
'''redis basic'''
import redis
import uuid
from typing import Any, Callable

class Cache:
    def __init__(self) -> None:
        '''init method of the class'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data:Any)->Any:
        '''stores a value in a redis key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key:str, **kwargs:Callable)->Any:
        '''gets the value of a key'''
        value = self._redis.get(key)
        fn = kwargs.get('fn')
        if fn:
            return fn(value)
        else:
            return value
            
    def get_str(self, value:Any)->str:
        '''converts value to string'''
        return str(value)
    
    def get_int(self, value:Any)->int:
        '''converts value to int'''
        return int(value)
    

cache = Cache()
TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value