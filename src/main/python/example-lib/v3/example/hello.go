package main

import "C"
import "fmt"

//export Hello
func Hello() {
	fmt.Println("Hello from Go!")
}

//export HelloWorld
func HelloWorld(name *C.char) {
	fmt.Printf("Hello %s!\n", C.GoString(name))
}

func main() {}
