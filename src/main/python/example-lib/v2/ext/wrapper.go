package main

import "C"
import "fmt"

//export Hello
func Hello(message *C.char, count C.int) {
	hello(C.GoString(message), int(count))
}

//export Check
func Check() {
	fmt.Println("inside go entry")
}

func main() {}
