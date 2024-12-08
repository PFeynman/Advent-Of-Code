package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
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

func ArrayAtoi(array []string) (result []int) {
	for _, e := range array {
		x, _ := strconv.Atoi(e)
		result = append(result, x)
	}
	return
}

func main() {
	fileName := "input_test.txt"
	text := GetFileContent(fileName)

	rules := make(map[int][]int)
	var updates [][]int

	var splited []int
	var reading_rules bool = true
	for _, line := range text {
		if line == "" {
			reading_rules = false
			continue
		}

		if reading_rules {
			splited = ArrayAtoi(strings.Split(line, "|"))
			rules[splited[0]] = append(rules[splited[0]], splited[1])
		} else {
			updates = append(updates, ArrayAtoi(strings.Split(line, ",")))
		}
	}
	fmt.Println(rules)
	var constraints []int
	var correct_updates [][]int
	var valid bool
	for _, update := range updates {
		fmt.Println(update)
		valid = true
		for i, page := range update {
			fmt.Println(page)
			constraints = rules[page]
			for _, constraint := range constraints {
				fmt.Printf("Constrain %d, %d\n", constraint, slices.Index(update, constraint))
				if slices.Index(update, constraint) >= 0 && slices.Index(update, constraint) < i {
					valid = false
					break
				}
			}
			if !valid {
				break
			}
		}
		if valid {
			correct_updates = append(correct_updates, update)
		}
	}

	fmt.Println(correct_updates)
}
