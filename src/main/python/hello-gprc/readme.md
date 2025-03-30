# Hello Python GPRC

## Reference
- https://grpc.io/docs/languages/python/quickstart
- https://github.com/grpc/grpc/blob/master/examples/python/helloworld

```shell
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. --pyi_out=. example.proto
```