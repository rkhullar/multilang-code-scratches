import asyncio
import logging

import grpc
import example_pb2
import example_pb2_grpc


class Greeter(example_pb2_grpc.GreeterServicer):
    async def SayHello(self, request: example_pb2.HelloRequest, context: grpc.aio.ServicerContext) -> example_pb2.HelloReply:
        return example_pb2.HelloReply(message=f'hello {request.name}')


async def serve() -> None:
    server = grpc.aio.server()
    example_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
