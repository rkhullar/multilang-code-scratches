package main

import (
	"gotest.tools/assert"
	"testing"
)

func Test(t *testing.T) {
	t.Run("TestDefaultValue", func(t *testing.T) {
		assert.Equal(t, 0, DefaultValue[int]())
		assert.Equal(t, "", DefaultValue[string]())
	})
	t.Run("TestListOperations", func(t *testing.T) {
		dut := NewList[int]()
		assert.Equal(t, 0, dut.size)
		dut.Push(1)
		dut.Push(2)
		dut.Push(3)
		dut.Prepend(0)
		assert.Equal(t, 4, dut.size)
		arr := dut.toArray()
		assert.DeepEqual(t, []int{0, 1, 2, 3}, arr)
		val, _ := dut.Pop()
		assert.Equal(t, 3, val)
		dut.Push(4)
		val, _ = dut.Pop()
		assert.Equal(t, 4, val)
		val, _ = dut.Dequeue()
		assert.Equal(t, 0, val)
		arr = dut.toArray()
		assert.DeepEqual(t, []int{1, 2}, arr)
	})
	t.Run("TestEmptyPop", func(t *testing.T) {
		dut := NewList[string]()
		_, ok := dut.Pop()
		assert.Assert(t, !ok)
		_, ok = dut.Dequeue()
		assert.Assert(t, !ok)
	})
}
