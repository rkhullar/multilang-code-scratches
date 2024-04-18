build: clean
	go build -buildmode=c-shared -o local/libcore.so main.go

clean:
	@rm -rf local _obj

test: clean
	@go test

reset: clean
	@rm -f go.sum
	@go clean -modcache # remove download modules
	@go mod tidy # reinstall dependencies
