```shell
go get goa.design/goa/v3/...
go install goa.design/goa/v3/cmd/goa@latest
```

```shell
# goa gen <module-name>/design
goa gen github.com/rkhullar/python-java-scratches/src/main/go/projects/message-api/goa/design
```

```shell
# goa example <module-name>/design
goa example github.com/rkhullar/python-java-scratches/src/main/go/projects/message-api/goa/design
```

```shell
# go run <module-name>/cmd/message --http-port=8080
go run github.com/rkhullar/python-java-scratches/src/main/go/projects/message-api/goa/cmd/message --http-port=8080
```

## Regen Requirements
```shell
# remove download modules
go clean -modcache

# reinstall dependencies
go mod tidy
```

```shell
docker run -p 8081:8080 swaggerapi/swagger-ui
```

## Reference
- https://goa.design/docs/2-getting-started
- https://github.com/goadesign/examples/blob/master/basic

### Potential Future Work
- serve openapi docs from goa service by including the swagger-ui codebase
  - https://medium.com/@divious_1/build-a-go-restful-api-using-goa-that-scales-effortlessly-with-google-app-engine-and-are-67e32da8c828
