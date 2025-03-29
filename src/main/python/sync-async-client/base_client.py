from abc import ABC, abstractmethod
from dataclasses import dataclass

import httpx

from type_util import BuildResponseCallable, HandleResponseCallable, SyncAsync, SyncAsyncCallable, T


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

    def build_function(self, build_response: BuildResponseCallable, handle_response: HandleResponseCallable[T]) -> SyncAsyncCallable[T]:
        if self.enable_async:
            async def wrapper():
                response = await build_response()
                return handle_response(response)
        else:
            def wrapper():
                response = build_response()
                return handle_response(response)
        return wrapper

    def build_and_invoke_function(self, build_response: BuildResponseCallable, handle_response: HandleResponseCallable[T]) -> T:
        fn = self.build_function(build_response=build_response, handle_response=handle_response)
        return fn()
