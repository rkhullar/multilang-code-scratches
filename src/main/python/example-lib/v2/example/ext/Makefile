all: clean lib ffi

lib:
	go build -buildmode=c-shared -o out/libexample.so example.go wrapper.go

ffi:
	python build_ffi.py

clean:
	@rm -rf out
