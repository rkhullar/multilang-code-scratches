package main

import (
	"context"
	"github.com/aws/aws-lambda-go/lambda"
)

type HelloLambdaEvent struct {
	Message string `json:"message"`
	Count   int    `json:"count"`
}

func HandleRequest(ctx context.Context, event *HelloLambdaEvent) (*string, error) {
	result := "|"
	for i := 0; i < event.Count; i++ {
		result += event.Message + "|"
	}
	return &result, nil
}

func main() {
	//fmt.Println("hello world")
	lambda.Start(HandleRequest)
}
