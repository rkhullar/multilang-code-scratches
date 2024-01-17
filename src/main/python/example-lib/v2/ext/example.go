package main

import "C"
import "fmt"

//export hello
func hello(message string, count int) int {
	for i := 0; i < count; i++ {
		fmt.Println(message)
	}
	return count + 1
}

func main() {}
