package models

// GreetRequest defines the input payload for creating a message
type GreetRequest struct {
	Text string `json:"text" binding:"required,min=1"`
}

// Message represents a message object
type Message struct {
	ID   string `json:"id"`
	Text string `json:"text"`
}
