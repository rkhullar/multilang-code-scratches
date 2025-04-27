package messageapi

import (
	"context"
	"errors"
	"github.com/google/uuid"
	"github.com/rkhullar/python-java-scratches/src/main/go/projects/message-api/goa/gen/message"
	"sync"
)

// message service example implementation.
// The example methods log the requests and return zero values.
type messagesrvc struct {
	mu       sync.RWMutex
	messages map[string]*message.Message
}

// NewMessage returns the message service implementation.
func NewMessage() message.Service {
	return &messagesrvc{
		messages: make(map[string]*message.Message),
	}
}

// Create implements create.
func (s *messagesrvc) Create(ctx context.Context, p *message.CreatePayload) (res *message.Message, err error) {
	id := uuid.New().String()
	msg := &message.Message{ID: id, Text: p.Text}
	s.mu.Lock()
	defer s.mu.Unlock()
	s.messages[id] = msg
	return msg, nil
}

// List implements list.
func (s *messagesrvc) List(ctx context.Context) (res []*message.Message, err error) {
	s.mu.RLock()
	defer s.mu.RUnlock()
	result := make([]*message.Message, 0)
	for _, m := range s.messages {
		result = append(result, m)
	}
	return result, nil
}

// Read implements read.
func (s *messagesrvc) Read(ctx context.Context, p *message.ReadPayload) (res *message.Message, err error) {
	s.mu.RLock()
	defer s.mu.RUnlock()
	msg, ok := s.messages[p.ID]
	if !ok {
		return nil, errors.New("message not found")
	}
	return msg, nil
}
