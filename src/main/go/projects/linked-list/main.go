package main

import "fmt"

type ListNode[T any] struct {
	data T
	prev *ListNode[T]
	next *ListNode[T]
}

type List[T any] struct {
	head *ListNode[T]
	tail *ListNode[T]
	size uint
}

func NewList[T any]() *List[T] {
	return &List[T]{nil, nil, 0}
}

func (this *List[T]) Push(data T) {
	fmt.Printf("adding %v to list", data)
}

func (this *List[T]) String() string {
	return "list format"
}

func main() {
	dut := NewList[int]()
	fmt.Println("Hello world")
	fmt.Println(dut)
	dut.Push(7)
}
