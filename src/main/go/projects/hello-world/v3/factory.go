package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

type message struct {
	ID      string `json:"id"`
	Message string `json:"message"`
}

var messages = []message{
	{ID: "1", Message: "hello world 1"},
	{ID: "2", Message: "hello world 2"},
}

func getMessages(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, messages)
}

func CreateRouter() *gin.Engine {
	router := gin.Default()
	router.GET("/messages", getMessages)
	return router
}
