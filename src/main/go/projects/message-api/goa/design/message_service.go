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
		Result(CustomMessage)
		HTTP(func() {
			POST("/messages")
			Response(StatusCreated)
		})
	})

	Method("list", func() {
		Result(ArrayOf(CustomMessage))
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
		Result(CustomMessage)
		Error("not_found", NotFoundError)
		HTTP(func() {
			GET("/messages/{id}")
			Response(StatusOK)
			Response("not_found", StatusNotFound)
		})
	})
})
