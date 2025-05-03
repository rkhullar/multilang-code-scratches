ARG GO_VERSION=1.24.2
FROM golang:${GO_VERSION}-alpine AS builder
WORKDIR /app
COPY . .
RUN go build -o message-api github.com/rkhullar/python-java-scratches/src/main/go/projects/message-api/goa/cmd/message

FROM alpine:latest
WORKDIR /app
COPY gen/http/openapi3.json gen/http/openapi3.json
COPY --from=builder /app/message-api .
CMD ["./message-api", "--http-port=8080"]
