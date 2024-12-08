package main

import (
	"bufio"
	"os"
)

func GetFileContent(fileName string) (text []string) {
	file, err := os.Open(fileName)
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)

	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		text = append(text, scanner.Text())
	}

	file.Close()
	return
}

func main() {
	fileName := "input_test.txt"
	text := GetFileContent(fileName)

}
