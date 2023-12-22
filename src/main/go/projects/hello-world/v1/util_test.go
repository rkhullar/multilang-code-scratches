package main

import (
	"gotest.tools/assert"
	"testing"
)

func TestHandleRequest(t *testing.T) {
	t.Run("canary", func(t *testing.T) {
		assert.Equal(t, Add(1, 2), 3)
	})
}
