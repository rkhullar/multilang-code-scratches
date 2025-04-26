## First Time Setup
```shell
asdf set golang 1.24.2
go mod init main
```

```shell
go get github.com/gin-gonic/gin
go get github.com/swaggo/swag/cmd/swag
go get github.com/google/uuid
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