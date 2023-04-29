package main

import "C"

func Hello(message *C.char) *C.char {
	value := C.GoString(message)
	return C.CString(hello(value))
}

func main() {}
