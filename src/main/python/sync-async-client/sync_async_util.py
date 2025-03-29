import functools

from base_client import AbstractBaseClient


def sync_async(fn):
    @functools.wraps(fn)
    def decorator(self: AbstractBaseClient, *args, **kwargs):
        if self.enable_async:
            async def wrapper():
                response = await fn(self, *args, **kwargs)
                return fn(self, *args, response=response, **kwargs)
        else:
            def wrapper():
                response = fn(self, *args, **kwargs)
                return fn(self, *args, response=response, **kwargs)
        return wrapper()
    return decorator
