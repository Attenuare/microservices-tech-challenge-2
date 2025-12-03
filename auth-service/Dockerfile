FROM golang:1.22 AS builder

WORKDIR /auth-service
COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -o /auth-service


FROM alpine:3.21.5
WORKDIR /
COPY --from=builder /auth-service /auth-service


CMD ["/auth-service"]