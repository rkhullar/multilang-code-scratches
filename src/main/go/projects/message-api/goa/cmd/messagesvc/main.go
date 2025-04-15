package main

import (
	"context"
	"log"
	"net/http"
	"sync"

	messagesvr "github.com/yourname/messagesvc/gen/http/message/server"
	message "github.com/yourname/messagesvc/gen/message"

	"github.com/google/uuid"
	httpmdlwr "goa.design/goa/v3/http/middleware"
)

func main() {
	logger := log.New(log.Writer(), "", log.LstdFlags)
	mux := http.NewServeMux()
	handler := httpmdlwr.Log(httpmdlwr.RequestID(httpmdlwr.New(logger)))

	svc := NewMessageService()
	endpoints := message.NewEndpoints(svc)
	server := messagesvr.New(endpoints, mux, handler, nil)

	for _, m := range server.Mounts {
		logger.Printf("HTTP %q mounted on %s %s", m.Method, m.Verb, m.Pattern)
	}

	log.Fatal(http.ListenAndServe(":8080", handler(mux)))
}

type Message struct {
	ID   string
	Text string
}

type MessageService struct {
	mu       sync.Mutex
	messages map[string]Message
}

func NewMessageService() *MessageService {
	return &MessageService{
		messages: make(map[string]Message),
	}
}

func (s *MessageService) Create(ctx context.Context, p *message.CreatePayload) (*message.Message, error) {
	id := uuid.New().String()
	msg := Message{ID: id, Text: p.Text}

	s.mu.Lock()
	defer s.mu.Unlock()
	s.messages[id] = msg

	return &message.Message{ID: msg.ID, Text: msg.Text}, nil
}

func (s *MessageService) List(ctx context.Context) ([]*message.Message, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	var result []*message.Message
	for _, m := range s.messages {
		result = append(result, &message.Message{ID: m.ID, Text: m.Text})
	}
	return result, nil
}

func (s *MessageService) Read(ctx context.Context, p *message.ReadPayload) (*message.Message, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	msg, ok := s.messages[p.ID]
	if !ok {
		return nil, message.MakeNotFound("message with ID %s not found", p.ID)
	}
	return &message.Message{ID: msg.ID, Text: msg.Text}, nil
}
