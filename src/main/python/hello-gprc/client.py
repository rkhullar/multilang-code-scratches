import asyncio
import logging
import os

import grpc

from patch import patch_path

patch_path()
from protos.generated import example_pb2, example_pb2_grpc

async def main() -> None:
    server_host = os.environ.get('SERVER_HOST', '[::]')
    server_port = int(os.environ.get('SERVER_PORT', '50052'))
    async with grpc.aio.insecure_channel(f'{server_host}:{server_port}') as channel:
        stub = example_pb2_grpc.GreeterStub(channel)
        response = await stub.SayHello(example_pb2.HelloRequest(name='John'))
        print(response.message)


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(main())
