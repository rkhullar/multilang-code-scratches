test:
	@go test

reset:
	@rm -f go.sum
	@go clean -modcache # remove download modules
	@go mod tidy # reinstall dependencies
