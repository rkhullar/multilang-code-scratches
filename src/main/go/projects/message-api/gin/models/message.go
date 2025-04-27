package models

type CreateMessage struct {
	Text string `json:"text" binding:"required,min=1"`
}

type Message struct {
	ID   string `json:"id"`
	Text string `json:"text"`
}
