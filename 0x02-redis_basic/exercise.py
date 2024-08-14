#!/usr/bin/env python3
""" ..... """
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """ .... """

    def __init__(self):
        """ .... """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ .... """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    int,
                                                                    None]:
        """ .... """
        data = self._redis.get(key)

        if data is None:
            return None

        if fn is not None:
            return fn(data)

        return (data)

    def get_str(self, key: str) -> str:
        """ .... """
        data = self.get(key,
                        lambda x: x.decode('utf-8')
                        if isinstance(x, bytes)
                        else str(x))
        return str(data)

    def get_int(self, key: str) -> Union[int, str, None]:
        """ .... """
        data = self.get(key,
                        lambda x: int(x) if x.isdigit() else None)

        return data
