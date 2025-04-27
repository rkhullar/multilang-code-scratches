package design

import (
	. "goa.design/goa/v3/dsl"
)

var _ = Service("message", func() {
	Description("simple message service")

	Method("create", func() {
		Payload(func() {
			Field(1, "text", String, "Message text", func() {
				MinLength(1)
			})
			Required("text")
		})
		Result(Message)
		HTTP(func() {
			POST("/messages")
			Response(StatusCreated)
		})
	})

	Method("list", func() {
		Result(ArrayOf(Message))
		HTTP(func() {
			GET("/messages")
			Response(StatusOK)
		})
	})

	Method("read", func() {
		Payload(func() {
			Field(1, "id", String, "UUID of the message")
			Required("id")
		})
		Result(Message)
		HTTP(func() {
			GET("/messages/{id}")
			Response(StatusOK)
			Response("not_found", StatusNotFound)
		})
	})
})

/*
var Message = ResultType("application/vnd.message+json", func() {
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
*/
