all: clean build post_build

build:
	go build -buildmode=c-shared -o lib/libhello.so hello.go

post_build:
	@rm -rf lib/*.h

clean:
	@rm -rf lib
