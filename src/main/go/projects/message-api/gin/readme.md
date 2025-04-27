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

```shell
go install github.com/swaggo/swag/cmd/swag@latest
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