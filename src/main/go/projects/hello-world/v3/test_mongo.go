package main

import (
	"fmt"
	"go.mongodb.org/mongo-driver/bson"
	"os"
)

func main() {
	_, localMode := os.LookupEnv("LOCAL_MODE")
	client := BuildAtlasClient(os.Getenv("ATLAS_HOST"), localMode)
	collection := client.Database("default").Collection("message")
	result := FindOneJson(collection, bson.D{{}})
	fmt.Println(result)
}
