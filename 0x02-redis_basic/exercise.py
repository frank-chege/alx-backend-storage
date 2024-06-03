#!/usr/bin/env python3
'''redis basic'''
import redis
import uuid
from typing import Any, Callable
from functools import wraps

key = ''
inkey = ''
outkey = ''
def count_calls(method:Callable)->callable:
    '''counts the no. of times a method is called'''
    @wraps(method)
    def wrapper(self, data:Any)->Any:
        '''wrapper function'''
        global key
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, data)
    return wrapper

def call_history(method:Callable)->Callable:
    '''appends input and output of a method to lists'''
    @wraps(method)
    def wrapper(self, data:Any)->Any:
        '''wrapper function'''
        global inkey
        global outkey
        inkey = method.__qualname__ + ':inputs'
        outkey = method.__qualname__ + ':outputs'
        self._redis.rpush(inkey, str(data))
        output = method(self, data)
        self._redis.rpush(outkey, output)
        return output
    return wrapper

def replay(method:Callable)->None:
    '''display the history of calls'''
    _redis = redis.Redis()
    count = _redis.get(key).decode('UTF-8')
    name = method.__qualname__
    in_list = _redis.lrange(inkey, 0, -1)
    out_list = _redis.lrange(outkey, 0, -1)
    print(f'{name} was called {count} times:')
    for inp, out in zip(in_list, out_list):
        print(f'{name}(*({inp.decode("UTF-8")},)) -> {out.decode("UTF-")}')

class Cache:
    def __init__(self) -> None:
        '''init method of the class'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

cache.store("foo")
cache.store("bar")
replay(cache.store)