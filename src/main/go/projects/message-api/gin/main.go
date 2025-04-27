package main

import (
	"github.com/gin-gonic/gin"
	_ "github.com/rkhullar/python-java-scratches/src/main/go/projects/message-api/gin/docs"
	"github.com/rkhullar/python-java-scratches/src/main/go/projects/message-api/gin/handlers"
	swaggerFiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
)

// @title Message API
// @version 1.0
// @description Simple API for storing and retrieving messages.
// @host localhost:8080
// @BasePath /
func main() {
	r := gin.Default()
	r.GET("/docs/*any", ginSwagger.WrapHandler(swaggerFiles.Handler))
	r.POST("/messages", handlers.CreateMessage)
	r.GET("/messages", handlers.ListMessages)
	r.GET("/messages/:id", handlers.ReadMessage)
	r.Run(":8080")
}
