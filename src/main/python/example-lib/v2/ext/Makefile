all: clean build

build:
	go build -buildmode=c-shared -o out/libexample.so example.go wrapper.go

clean:
	@rm -rf out
