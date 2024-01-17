all: clean build

build:
	go build -buildmode=c-shared -o out/libexample.so example.go

clean:
	@rm -rf out
