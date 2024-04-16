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
	// add to end of list
	node := NewListNode(data)
	if this.size < 1 {
		this.head = node
		this.tail = node
	} else {
		curr := this.tail
		curr.next = node
		node.prev = curr
		this.tail = node
	}
	this.size += 1
}

func (this *List[T]) Pop() T {
	// remote from end of list
	fmt.Printf("remove from end of list\n")
	node := this.tail
	return node.data
}

func (this *List[T]) Prepend(data T) {
	// add to start of list
	fmt.Printf("add %v to start of list\n", data)
}

func (this *List[T]) Dequeue() {
	// remove from start of list
	fmt.Printf("remove from start of list\n")
}

func (this *List[T]) String() string {
	curr := this.head
	for curr != nil {
		fmt.Println(curr.data)
		curr = curr.next
	}
	return "list format"
}

func (this *List[T]) toArray() []T {
	arr := make([]T, this.size)
	return arr
}

func main() {
	dut := NewList[int]()
	//a := NewListNode(1)
	//b := NewListNode(2)
	//c := NewListNode(3)
	//a.next = b
	//b.prev = a
	//b.next = c
	//c.prev = b
	//dut.head = a
	//dut.tail = c
	//dut.size = 3
	fmt.Println("Hello world")
	fmt.Println(dut)
	dut.Push(1)
	dut.Push(2)
	dut.Push(3)
	//arr := dut.toArray()
	//fmt.Println(arr)
}
