package design

import (
	. "goa.design/goa/v3/dsl"
)

var NotFoundError = Type("NotFoundError", func() {
	Field(1, "message", String, "error message")
	Required("message")
})
