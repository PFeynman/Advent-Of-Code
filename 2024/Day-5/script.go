package main

import (
	"bufio"
	"fmt"
	"math"
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

func SolutionOne(rules map[int][]int, updates [][]int) int {
	var constraints []int
	var correct_updates [][]int
	var valid bool
	sum := 0
	for _, update := range updates {
		valid = true
		for i, page := range update {
			constraints = rules[page]
			for _, constraint := range constraints {
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
			sum += update[int(math.Floor(float64(len(update)/2)))]
		}
	}

	return sum
}

func SolutionTwo(rules map[int][]int, updates [][]int) int {
	var constraints []int
	var incorrect_updates [][]int
	var valid bool
	var index int

	sum := 0
	for _, update := range updates {
		valid = true
		for i, page := range update {
			constraints = rules[page]
			for _, constraint := range constraints {
				index = slices.Index(update, constraint)
				if index >= 0 && index < i {
					update = slices.Delete(update, i, i+1)
					update = slices.Insert(update, index, page)
					valid = false
					i = index
				}
			}
		}
		if !valid {
			incorrect_updates = append(incorrect_updates, update)
			sum += update[int(math.Floor(float64(len(update)/2)))]
		}
	}
	return sum
}

func main() {
	fileName := "input.txt"
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

	fmt.Printf("Solution One: %d\n", SolutionOne(rules, updates))
	fmt.Printf("Solution Two: %d\n", SolutionTwo(rules, updates))
}
