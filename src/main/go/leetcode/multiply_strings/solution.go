package main

import (
	"strings"
)

type BigInteger struct {
	digits []byte
}

func ParseBigInteger(number string) *BigInteger {
	size := len(number)
	digits := make([]byte, size)
	for i, c := range number {
		digits[i] = byte(c - '0')
	}
	return &BigInteger{digits}
}

func (this BigInteger) String() string {
	var sb strings.Builder
	for _, digit := range this.digits {
		sb.WriteByte(digit + '0')
	}
	return sb.String()
}

func multiply(num1 string, num2 string) string {
	return ""
}
