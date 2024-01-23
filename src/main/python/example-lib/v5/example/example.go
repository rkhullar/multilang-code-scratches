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

//export HelloWorldNTimes
func HelloWorldNTimes(message *C.char, count C.int) {
	helloWorldNTimes(C.GoString(message), int(count))
}

//export Reverse
func Reverse(text *C.char) *C.char {
	return C.CString(reverse(C.GoString(text)))
}

func helloWorldNTimes(message string, count int) {
	for i := 0; i < count; i++ {
		fmt.Println(message)
	}
}

func reverse(text string) string {
	arr := []rune(text)
	for i, j := 0, len(arr)-1; i < len(arr)/2; i, j = i+1, j-1 {
		arr[i], arr[j] = arr[j], arr[i]
	}
	return string(arr)
}

func main() {}
