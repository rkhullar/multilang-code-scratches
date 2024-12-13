from dataclasses import dataclass
from base_client import AbstractBaseClient
from type_util import SyncAsync
import httpx


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
