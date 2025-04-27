## First Time Setup
```shell
asdf set golang 1.24.2
go mod init main # rename afterwards
```

```shell
go get github.com/gin-gonic/gin
go get github.com/swaggo/swag/cmd/swag
go get github.com/google/uuid
```


## Generating Docs
```shell
go install github.com/swaggo/swag/cmd/swag@latest
```
```shell
swag init
```

## Regen Requirements
```shell
# remove download modules
go clean -modcache

# reinstall dependencies
go mod tidy
```

## Running Locally
```shell
go run main.go
```

## OpenAPI Docs
- http://localhost:8080/swagger/index.html

#### Other
- swag init issue with left and right delim
  - https://github.com/swaggo/swag/issues/1568
  - `go get -u github.com/swaggo/swag`
