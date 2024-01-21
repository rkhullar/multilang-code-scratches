all: clean build

build:
	go build -buildmode=c-shared -o local/libexample.so example.go

clean:
	@rm -rf local
