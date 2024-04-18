build: clean
	go build -buildmode=c-shared -o local/liblinkedlist.so core.go

clean:
	@rm -rf local _obj

test: clean
	@go test

reset: clean
	@rm -f go.sum
	@go clean -modcache # remove download modules
	@go mod tidy # reinstall dependencies
