package design

import (
	. "goa.design/goa/v3/dsl"
)

var _ = API("message", func() {
	Title("simple message service")
	Description("hello world http service for managing messages")
	Server("message", func() {
		Description("hosts the message service")
		Services("message")
		Host("development", func() {
			Description("development hosts")
			URI("http://localhost:8080/message")
		})
	})
})

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

	Files("/openapi.json", "gen/http/openapi3.json")
})

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
