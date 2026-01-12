<<<<<<< HEAD
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
=======


FROM golang:1.22 AS builder

WORKDIR /app

COPY . .

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o app

FROM gcr.io/distroless/base-debian12

WORKDIR /app

COPY --from=builder /app/app .

CMD ["./app"]
>>>>>>> 0c89916db050eb69c1dddb8c5df1c6c1b7c7ab27
