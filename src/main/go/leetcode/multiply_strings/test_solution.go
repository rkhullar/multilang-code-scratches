package main

import (
	"fmt"
)

func testPlus() {
	a, b := "999", "1"
	y := ParseBigInteger(a).plus(ParseBigInteger(b))
	fmt.Println(y.String())
}

func testMultiply() {
	a, b := "123", "456"
	y := multiply(a, b)
	fmt.Println(y)
}

func main() {
	// testPlus()
	testMultiply()
}
