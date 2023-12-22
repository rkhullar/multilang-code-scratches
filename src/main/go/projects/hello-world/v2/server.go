package main

func main() {
	router := CreateRouter()
	router.Run("localhost:8000")
}
