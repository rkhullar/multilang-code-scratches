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
}
