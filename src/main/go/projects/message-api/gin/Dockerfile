ARG GO_VERSION=1.24.2
FROM golang:${GO_VERSION}-alpine AS builder

WORKDIR /app
COPY . .

RUN go build -o message-api

FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/message-api .

CMD ["./message-api"]
