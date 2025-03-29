"""
NOTE: This module was for supporting ExampleClient.read_pets_v2; but that method is not working for async.
"""

import functools

from base_client import AbstractBaseClient


def sync_async(fn):
    @functools.wraps(fn)
    def decorator(self: AbstractBaseClient, *args, **kwargs):
        if self.enable_async:
            async def wrapper():
                generator = fn(self, *args, **kwargs)
                response = await next(generator)
                generator = fn(self, *args, response=response, **kwargs)
                return next(generator)
        else:
            def wrapper():
                generator = fn(self, *args, **kwargs)
                response = next(generator)
                return fn(self, *args, response=response, **kwargs)
        return wrapper()
    return decorator
