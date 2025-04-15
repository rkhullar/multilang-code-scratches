package main

import (
	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
	"net/http"
	"sync"
)

type GreetRequest struct {
	Text string `json:"text" binding:"required,min=1"`
}

type Message struct {
	ID   string `json:"id"`
	Text string `json:"text"`
}

var messages = make(map[string]Message)
var mu sync.Mutex

func main() {
	r := gin.Default()

	// Create message
	r.POST("/messages", func(c *gin.Context) {
		var req GreetRequest
		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		id := uuid.New().String()
		msg := Message{ID: id, Text: req.Text}
		mu.Lock()
		messages[id] = msg
		mu.Unlock()
		c.JSON(http.StatusCreated, msg)
	})

	// List messages
	r.GET("/messages", func(c *gin.Context) {
		mu.Lock()
		var result []Message
		for _, m := range messages {
			result = append(result, m)
		}
		mu.Unlock()
		c.JSON(http.StatusOK, result)
	})

	// Read message by ID
	r.GET("/messages/:id", func(c *gin.Context) {
		id := c.Param("id")
		mu.Lock()
		msg, ok := messages[id]
		mu.Unlock()
		if !ok {
			c.JSON(http.StatusNotFound, gin.H{"error": "Message not found"})
			return
		}
		c.JSON(http.StatusOK, msg)
	})

	r.Run(":8080")
}
