package main

import "C"

//export Hello
func Hello(message *C.char, count C.int) {
	hello(C.GoString(message), int(count))
}

func main() {}
