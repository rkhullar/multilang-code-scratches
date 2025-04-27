package design

import (
	. "goa.design/goa/v3/dsl"
)

var CustomMessage = ResultType("application/vnd.message+json", func() {
	TypeName("Message")
	Attributes(func() {
		Attribute("id", String, "UUID of the message")
		Attribute("text", String, "Message text")
		Required("id", "text")
	})
	View("default", func() {
		Attribute("id")
		Attribute("text")
	})
})
