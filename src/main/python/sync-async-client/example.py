import httpx
from dataclasses import dataclass
from typing import Awaitable, TypeVar, Callable
from abc import ABC, abstractmethod


T = TypeVar('T')
SyncAsync = T | Awaitable[T]


'''
import functools
from typing import Type
ClientType = TypeVar('ClientType', bound='AbstractBaseClient')

def decorate(fn: Callable[..., T]) -> Callable[..., SyncAsync[T]]:
    @functools.wraps(fn)
    def wrapper(self: Type[ClientType], *args, **kwargs):
        if self.enable_async:
            async def inner_wrapper() -> Awaitable[T]:
                return await fn(self, *args, **kwargs)
        else:
            def inner_wrapper() -> T:
                return fn(self, *args, **kwargs)
        return inner_wrapper()
    return wrapper
'''


@dataclass
class AbstractBaseClient(ABC):
    enable_async: bool = False

    def __post_init__(self):
        httpx_class = httpx.AsyncClient if self.enable_async else httpx.Client
        self.client = httpx_class(**self.build_client_params())

    @abstractmethod
    def build_client_params(self) -> dict:
        pass

    def send_request(self, method: str, *args, **kwargs) -> SyncAsync[httpx.Response]:
        fn = getattr(self.client, method)
        return fn(*args, **kwargs)

    def build_function(self, build_response: Callable[[], httpx.Response], handle_response: Callable[[httpx.Response], T]) -> Callable[[], SyncAsync[T]]:
        if self.enable_async:
            async def wrapper():
                response = await build_response()
                return handle_response(response)
        else:
            def wrapper():
                response = build_response()
                return handle_response(response)
        return wrapper


@dataclass
class ExampleClient(AbstractBaseClient):
    base_url: str = 'http://petstore-demo-endpoint.execute-api.com'

    def build_client_params(self) -> dict:
        return dict(base_url=self.base_url)

    def read_pets(self) -> SyncAsync[list[dict]]:
        def handle_response(response: httpx.Response) -> list[dict]:
            response.raise_for_status()
            return response.json()

        return self.build_function(
            build_response=lambda: self.send_request(method='get', url='/petstore/pets'),
            handle_response=handle_response
        )()


def test_sync():
    print('test sync')
    client = ExampleClient(enable_async=False)
    result = client.read_pets()
    print(result)


async def test_async():
    print('test async')
    client = ExampleClient(enable_async=True)
    result = await client.read_pets()
    print(result)


async def main():
    test_sync()
    await test_async()


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
