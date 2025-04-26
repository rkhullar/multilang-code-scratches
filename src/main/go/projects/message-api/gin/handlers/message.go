package handlers

import (
	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
	"main/models"
	"net/http"
	"sync"
)

var (
	messages = make(map[string]models.Message)
	mu       sync.Mutex
)

// CreateMessage handles POST /messages
func CreateMessage(c *gin.Context) {
	var req models.GreetRequest
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	id := uuid.New().String()
	msg := models.Message{ID: id, Text: req.Text}

	mu.Lock()
	messages[id] = msg
	mu.Unlock()

	c.JSON(http.StatusCreated, msg)
}

// ListMessages handles GET /messages
func ListMessages(c *gin.Context) {
	mu.Lock()
	var result []models.Message
	for _, m := range messages {
		result = append(result, m)
	}
	mu.Unlock()
	c.JSON(http.StatusOK, result)
}

// ReadMessage handles GET /messages/{id}
func ReadMessage(c *gin.Context) {
	id := c.Param("id")

	mu.Lock()
	msg, ok := messages[id]
	mu.Unlock()

	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "Message not found"})
		return
	}
	c.JSON(http.StatusOK, msg)
}
