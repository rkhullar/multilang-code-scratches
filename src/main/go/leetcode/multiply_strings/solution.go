package main

import (
	"strings"
)

type BigInteger struct {
	digits []byte
}

func NewBigInteger(size int) *BigInteger {
	return &BigInteger{make([]byte, size)}
}

func ParseBigInteger(number string) *BigInteger {
	result := NewBigInteger(len(number))
	for i, c := range number {
		result.digits[i] = byte(c - '0')
	}
	return result
}

func (this BigInteger) String() string {
	var sb strings.Builder
	for _, digit := range this.digits {
		sb.WriteByte(digit + '0')
	}
	return sb.String()
}

func (this BigInteger) plus(other *BigInteger) *BigInteger {
	size := max(len(this.digits), len(other.digits))
	result := NewBigInteger(size + 1)
	var carry byte = 0
	for i := 0; i < size; i++ {
		var a byte = this.digitAt(size - i - 1)
		var b byte = other.digitAt(size - i - 1)
		var sum byte = a + b + carry
		carry = sum / 10
		result.digits[size-i] = sum % 10

	}
	result.digits[0] = carry
	return result
}

func (this BigInteger) digitAt(index int) byte {
	if 0 <= index && index < len(this.digits) {
		return this.digits[index]
	} else {
		return 0
	}
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func multiply(num1 string, num2 string) string {
	return ""
}
