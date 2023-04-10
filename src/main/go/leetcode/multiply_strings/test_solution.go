package main

import (
	"fmt"
)

func main() {
	a := ParseBigInteger("123")
	b := ParseBigInteger("456")
	fmt.Println(a.plus(b))
}
