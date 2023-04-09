package main

import "fmt"

type BigInteger struct {
	digits []byte
}

/*
func NewBigInteger(size int) *BigInteger {
	return &BigInteger{make([]byte, size)}
}
*/

func ParseBigInteger(number string) *BigInteger {
	size := len(number)
	digits := make([]byte, size)
	for i, c := range number {
		digits[i] = byte(c - '0')
	}
	return &BigInteger{digits}
}

//func multiply(num1 string, num2 string) string {
//
//}

func main() {
	fmt.Println("Hello, World!")
	fmt.Println(ParseBigInteger("123"))
}
