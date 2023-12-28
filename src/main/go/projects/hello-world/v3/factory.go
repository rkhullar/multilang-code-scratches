package main

import (
	"context"
	"fmt"
	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"net/http"
	"os"
)

type message struct {
	ID      string `json:"id"`
	Message string `json:"message"`
}

var messages = []message{
	{ID: "1", Message: "hello world 1"},
	{ID: "2", Message: "hello world 2"},
}

func BuildAtlasClient(atlasHost string) *mongo.Client {
	mongoClientUrl := fmt.Sprintf("mongodb+srv://%s/?authSource=%%24external&authMechanism=MONGODB-AWS&retryWrites=true&w=majority", atlasHost)
	serverApi := options.ServerAPI(options.ServerAPIVersion1)
	opts := options.Client().ApplyURI(mongoClientUrl).SetServerAPIOptions(serverApi)
	client, err := mongo.Connect(context.TODO(), opts)
	if err != nil {
		panic(err)
	}
	return client
}

func getMessages(c *gin.Context) {
	client := BuildAtlasClient(os.Getenv("ATLAS_HOST"))
	fmt.Println(client)
	c.IndentedJSON(http.StatusOK, messages)
}

func CreateRouter() *gin.Engine {
	router := gin.Default()
	router.GET("/messages", getMessages)
	return router
}
