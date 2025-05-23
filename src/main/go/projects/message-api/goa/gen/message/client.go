// Code generated by goa v3.20.1, DO NOT EDIT.
//
// message client
//
// Command:
// $ goa gen
// github.com/rkhullar/python-java-scratches/src/main/go/projects/message-api/goa/design

package message

import (
	"context"

	goa "goa.design/goa/v3/pkg"
)

// Client is the "message" service client.
type Client struct {
	CreateEndpoint goa.Endpoint
	ListEndpoint   goa.Endpoint
	ReadEndpoint   goa.Endpoint
}

// NewClient initializes a "message" service client given the endpoints.
func NewClient(create, list, read goa.Endpoint) *Client {
	return &Client{
		CreateEndpoint: create,
		ListEndpoint:   list,
		ReadEndpoint:   read,
	}
}

// Create calls the "create" endpoint of the "message" service.
func (c *Client) Create(ctx context.Context, p *CreatePayload) (res *Message, err error) {
	var ires any
	ires, err = c.CreateEndpoint(ctx, p)
	if err != nil {
		return
	}
	return ires.(*Message), nil
}

// List calls the "list" endpoint of the "message" service.
func (c *Client) List(ctx context.Context) (res []*Message, err error) {
	var ires any
	ires, err = c.ListEndpoint(ctx, nil)
	if err != nil {
		return
	}
	return ires.([]*Message), nil
}

// Read calls the "read" endpoint of the "message" service.
// Read may return the following errors:
//   - "not_found" (type *NotFoundError)
//   - error: internal error
func (c *Client) Read(ctx context.Context, p *ReadPayload) (res *Message, err error) {
	var ires any
	ires, err = c.ReadEndpoint(ctx, p)
	if err != nil {
		return
	}
	return ires.(*Message), nil
}
