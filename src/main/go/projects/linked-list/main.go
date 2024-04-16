package main

import "fmt"

type ListNode[T any] struct {
	data T
	prev *ListNode[T]
	next *ListNode[T]
}

func NewListNode[T any](data T) *ListNode[T] {
	return &ListNode[T]{data, nil, nil}
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
	curr := this.head
	for curr != nil {
		fmt.Println(curr.data)
		curr = curr.next
	}
	return "list format"
}

func main() {
	dut := NewList[int]()
	a := NewListNode(1)
	b := NewListNode(2)
	c := NewListNode(3)
	a.next = b
	b.prev = a
	b.next = c
	c.prev = b
	dut.head = a
	dut.tail = c
	dut.size = 3
	fmt.Println("Hello world")
	fmt.Println(dut)
	dut.Push(7)
}
