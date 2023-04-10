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
	wroteFirstDigit := false
	for _, digit := range this.digits {
		if wroteFirstDigit || digit != 0 {
			sb.WriteByte(digit + '0')
			wroteFirstDigit = true
		}
	}
	if !wroteFirstDigit {
		sb.WriteByte(0 + '0')
	}
	return sb.String()
}

func (this BigInteger) size() int {
	return len(this.digits)
}

func (this BigInteger) plus(other *BigInteger) *BigInteger {
	size := max(this.size(), other.size())
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

func (this BigInteger) multiply(other *BigInteger) *BigInteger {
	size := other.size()
	product := NewBigInteger(0)
	for i := 0; i < size; i++ {
		addend := this.partialMultiply(other.digits[size-i-1], i)
		product = product.plus(addend)
	}
	return product
}

func (this BigInteger) partialMultiply(otherFactor byte, place int) *BigInteger {
	size := this.size()
	result := NewBigInteger(size + place + 1)
	var carry byte = 0
	for i := 0; i < size; i++ {
		var thisFactor byte = this.digits[size-i-1]
		var product = thisFactor*otherFactor + carry
		carry = product / 10
		result.digits[size-i] = product % 10
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
	a, b := ParseBigInteger(num1), ParseBigInteger(num2)
	return a.multiply(b).String()
}
