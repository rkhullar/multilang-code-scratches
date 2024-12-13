from dataclasses import dataclass

import httpx

from base_client import AbstractBaseClient
from type_util import SyncAsync

import functools


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


@dataclass
class ExampleClient(AbstractBaseClient):
    base_url: str = 'http://petstore-demo-endpoint.execute-api.com'

    def build_client_params(self) -> dict:
        return dict(base_url=self.base_url)

    def read_pets(self) -> SyncAsync[list[dict]]:
        def handle_response(response: httpx.Response) -> list[dict]:
            response.raise_for_status()
            return response.json()

        return self.build_and_invoke_function(
            build_response=lambda: self.send_request(method='get', url='/petstore/pets'),
            handle_response=handle_response
        )

    @sync_async
    def read_pets_v2(self, response: httpx.Response = None):
        if not response:
            yield self.send_request(method='get', url='/petstore/pets')
        response.raise_for_status()
        return response.json()
