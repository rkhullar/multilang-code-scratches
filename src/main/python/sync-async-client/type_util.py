from typing import Awaitable, Callable, TypeVar

import httpx

T = TypeVar('T')
SyncAsync = T | Awaitable[T]
BuildResponseCallable = Callable[[], httpx.Response]
HandleResponseCallable = Callable[[httpx.Response], T]
SyncAsyncCallable = Callable[[], SyncAsync[T]]
