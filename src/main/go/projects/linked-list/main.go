package main

import (
	"fmt"
	"strings"
)

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

func DefaultValue[T any]() T {
	var value T
	return value
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

func (this *List[T]) Pop() (T, bool) {
	// remove from end of list
	if this.size < 1 {
		return DefaultValue[T](), false
	} else {
		node := this.tail
		curr := node.prev
		if curr != nil {
			curr.next = nil
		}
		node.prev = nil
		node.next = nil
		this.tail = curr
		this.size -= 1
		return node.data, true
	}
}

func (this *List[T]) Prepend(data T) {
	// add to start of list
	node := NewListNode(data)
	if this.size < 1 {
		this.head = node
		this.tail = node
	} else {
		node.next = this.head
		this.head.prev = node
		this.head = node
	}
	this.size += 1
}

func (this *List[T]) Dequeue() (T, bool) {
	// remove from start of list
	if this.size < 1 {
		return DefaultValue[T](), false
	} else {
		node := this.head
		curr := node.next
		if curr != nil {
			curr.prev = nil
		}
		node.prev = nil
		node.next = nil
		this.head = curr
		this.size -= 1
		return node.data, true
	}
}

func (this *List[T]) IterNode() <-chan *ListNode[T] {
	channel := make(chan *ListNode[T])
	go func() {
		defer close(channel)
		curr := this.head
		for curr != nil {
			channel <- curr
			curr = curr.next
		}
	}()
	return channel
}

func (this *List[T]) IterData() <-chan T {
	channel := make(chan T)
	go func() {
		defer close(channel)
		curr := this.head
		for curr != nil {
			channel <- curr.data
			curr = curr.next
		}
	}()
	return channel
}

func (this *List[T]) String() string {
	var builder strings.Builder
	builder.WriteString("[")
	for node := range this.IterNode() {
		separator := " "
		if node.next == nil {
			separator = ""
		}
		toWrite := fmt.Sprintf("%v%s", node.data, separator)
		builder.WriteString(toWrite)
	}
	builder.WriteString("]")
	return builder.String()
}

func (this *List[T]) toArray() []T {
	arr := make([]T, this.size)
	index := 0
	for item := range this.IterData() {
		arr[index] = item
		index += 1
	}
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
	fmt.Println("hello world")
	dut.Push(1)
	dut.Push(2)
	dut.Push(3)
	value, ok := dut.Pop()
	if ok {
		fmt.Println(value)
	}
	fmt.Println(dut)
	arr := dut.toArray()
	fmt.Println(arr)
}
