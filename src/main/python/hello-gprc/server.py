import asyncio
import logging
import os

import grpc

from patch import patch_path

patch_path()
from protos.generated import example_pb2, example_pb2_grpc


class Greeter(example_pb2_grpc.GreeterServicer):
    async def SayHello(self, request: example_pb2.HelloRequest, context: grpc.aio.ServicerContext) -> example_pb2.HelloReply:
        return example_pb2.HelloReply(message=f'hello {request.name}')


async def serve() -> None:
    server_host = os.environ.get('SERVER_HOST', '[::]')
    server_port = int(os.environ.get('SERVER_PORT', '50052'))
    server = grpc.aio.server()
    example_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    listen_addr = f'{server_host}:{server_port}'
    server.add_insecure_port(listen_addr)
    logging.info("starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    patch_path()
    asyncio.run(serve())
