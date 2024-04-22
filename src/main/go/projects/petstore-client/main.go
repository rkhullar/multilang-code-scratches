package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

type PetStoreClient struct {
	baseUrl string
}

func NewPetStoreClient() *PetStoreClient {
	return &PetStoreClient{"http://petstore-demo-endpoint.execute-api.com/petstore/pets"}
}

func HttpGetBody(url string) (string, error) {
	res, err := http.Get(url)
	if err != nil {
		return "", err
	} else {
		body, err := io.ReadAll(res.Body)
		if err != nil {
			return "", err
		} else {
			return string(body), nil
		}
	}
}

type ByteSlice []byte
type StringMap map[string]any
type JsonList []StringMap

func ParseJsonList(json_data string) (JsonList, error) {
	var result JsonList
	err := json.Unmarshal(ByteSlice(json_data), &result)
	if err != nil {
		return nil, err
	}
	return result, nil
}

func HttpGetJsonList(url string) (JsonList, error) {
	body, err := HttpGetBody(url)
	if err != nil {
		return nil, err
	} else {
		data, err := ParseJsonList(body)
		if err != nil {
			return nil, err
		} else {
			return data, nil
		}
	}
}

func (this *PetStoreClient) TestRead() {
	result, err := HttpGetJsonList(this.baseUrl)
	if err == nil {
		fmt.Println(result)
	}
}

func main() {
	client := NewPetStoreClient()
	client.TestRead()
}
