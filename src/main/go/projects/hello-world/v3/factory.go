package main

import (
	"context"
	"encoding/json"
	"fmt"
	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/bson"
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

func LoadAWSVars() aws.Credentials {
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		panic(err)
	}
	vars, err := cfg.Credentials.Retrieve(context.TODO())
	if err != nil {
		panic(err)
	}
	return vars
}

func BuildAtlasClient(atlasHost string, local bool) *mongo.Client {
	//mongoClientUrl := fmt.Sprintf("mongodb+srv://%s/?authSource=%%24external&authMechanism=MONGODB-AWS&retryWrites=true&w=majority", atlasHost)
	mongoClientUrl := fmt.Sprintf("mongodb+srv://%s/?retryWrites=true&w=majority", atlasHost)
	serverApi := options.ServerAPI(options.ServerAPIVersion1)
	credential := options.Credential{
		AuthMechanism: "MONGODB-AWS",
		AuthSource:    "$external",
	}
	if local {
		awsVars := LoadAWSVars()
		credential.Username = awsVars.AccessKeyID
		credential.Password = awsVars.SecretAccessKey
		credential.AuthMechanismProperties = map[string]string{
			"AWS_SESSION_TOKEN": awsVars.SessionToken,
		}
	}
	opts := options.Client().ApplyURI(mongoClientUrl).SetServerAPIOptions(serverApi).SetAuth(credential)
	client, err := mongo.Connect(context.TODO(), opts)
	if err != nil {
		panic(err)
	}
	return client
}

func FindOneJson(collection *mongo.Collection, filter bson.D) string {
	var result bson.M
	err := collection.FindOne(context.TODO(), filter).Decode(&result)
	if err != nil {
		panic(err)
	}
	jsonData, err := json.Marshal(result)
	if err != nil {
		panic(err)
	}
	return string(jsonData)
}

var _, localMode = os.LookupEnv("LOCAL_MODE")
var client = BuildAtlasClient(os.Getenv("ATLAS_HOST"), localMode)

func getMessages(c *gin.Context) {
	collection := client.Database("default").Collection("message")
	var result bson.M
	err := collection.FindOne(context.TODO(), bson.D{{}}).Decode(&result)
	if err != nil {
		panic(err)
	}
	jsonData, err := json.Marshal(result)
	if err != nil {
		panic(err)
	}
	fmt.Println(jsonData)
	c.IndentedJSON(http.StatusOK, messages)
}

func CreateRouter() *gin.Engine {
	router := gin.Default()
	router.GET("/messages", getMessages)
	client.Ping(context.TODO(), nil)
	return router
}
