package handlers

import (
	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
	"github.com/rkhullar/python-java-scratches/src/main/go/projects/message-api/gin/models"
	"net/http"
	"sync"
)

var (
	messages = make(map[string]models.Message)
	mu       sync.RWMutex
)

// CreateMessage
// @Summary create message
// @Accept json
// @Produce json
// @Param message body models.Message true "Message to create"
// @Success 201 {object} models.Message
// @Router /messages [post]
func CreateMessage(c *gin.Context) {
	var req models.CreateMessage
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	id := uuid.New().String()
	msg := models.Message{ID: id, Text: req.Text}
	mu.Lock()
	defer mu.Unlock()
	messages[id] = msg
	c.JSON(http.StatusCreated, msg)
}

// ListMessages
// @Summary list messages
// @Produce json
// @Success 200 {array} models.Message
// @Router /messages [get]
func ListMessages(c *gin.Context) {
	mu.RLock()
	defer mu.RUnlock()
	var result []models.Message
	for _, m := range messages {
		result = append(result, m)
	}
	c.JSON(http.StatusOK, result)
}

// ReadMessage
// @Summary read message
// @Produce json
// @Param id path string true "Message ID"
// @Success 200 {object} models.Message
// @Failure 404 {object} gin.H
// @Router /messages/{id} [get]
func ReadMessage(c *gin.Context) {
	id := c.Param("id")
	mu.RLock()
	defer mu.RUnlock()
	msg, ok := messages[id]
	if !ok {
		c.JSON(http.StatusNotFound, gin.H{"error": "message not found"})
		return
	}
	c.JSON(http.StatusOK, msg)
}
