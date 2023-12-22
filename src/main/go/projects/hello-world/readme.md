## Project Setup

#### Hello World
```shell
asdf local golang 1.21.5
go mod init main
go run .
```

```shell
go get github.com/aws/aws-lambda-go/lambda
```

##### Lambda Function Config
- name: test-hello-go
- runtime: Amazon Linux 2023
- architecture: arm64
- handler: bootstrap


#### Links
- https://go.dev/doc/tutorial/getting-started
- https://docs.aws.amazon.com/lambda/latest/dg/golang-handler.html
