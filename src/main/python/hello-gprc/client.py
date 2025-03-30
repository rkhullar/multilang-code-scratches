import asyncio
import logging

import grpc

from patch import patch_path

patch_path()
from protos.generated import example_pb2, example_pb2_grpc

async def main() -> None:
    async with grpc.aio.insecure_channel('localhost:50052') as channel:
        stub = example_pb2_grpc.GreeterStub(channel)
        response = await stub.SayHello(example_pb2.HelloRequest(name='John'))
        print(response.message)


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(main())
