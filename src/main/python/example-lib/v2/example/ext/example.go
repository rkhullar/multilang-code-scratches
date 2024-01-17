package main

import "fmt"

func hello(message string, count int) {
	for i := 0; i < count; i++ {
		fmt.Println(message)
	}
}
