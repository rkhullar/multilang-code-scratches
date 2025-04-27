package messageapi

import (
	"context"

	message "github.com/rkhullar/python-java-scratches/src/main/go/projects/message-api/goa/gen/message"
	"goa.design/clue/log"
)

// message service example implementation.
// The example methods log the requests and return zero values.
type messagesrvc struct{}

// NewMessage returns the message service implementation.
func NewMessage() message.Service {
	return &messagesrvc{}
}

// Create implements create.
func (s *messagesrvc) Create(ctx context.Context, p *message.CreatePayload) (res *message.Message, err error) {
	res = &message.Message{}
	log.Printf(ctx, "message.create")
	return
}

// List implements list.
func (s *messagesrvc) List(ctx context.Context) (res []*message.Message, err error) {
	log.Printf(ctx, "message.list")
	return
}

// Read implements read.
func (s *messagesrvc) Read(ctx context.Context, p *message.ReadPayload) (res *message.Message, err error) {
	res = &message.Message{}
	log.Printf(ctx, "message.read")
	return
}
