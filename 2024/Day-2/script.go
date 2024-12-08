package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func ArrayAtoi(array []string) (result []int) {
	for _, e := range array {
		x, _ := strconv.Atoi(e)
		result = append(result, x)
	}
	return
}

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

func IsSafe(report []int, calls int) bool {
	array_copy := make([]int, len(report))
	safe := false

	if report[0] < report[len(report)-1] {
		// Crece
		for i := 0; i < len(report)-1; i++ {
			if report[i] >= report[i+1] || report[i+1]-report[i] > 3 {
				if calls < 2 {
					i++
					copy(array_copy, report)
					array_copy = append(array_copy[:i], array_copy[i+1:]...)
					safe = IsSafe(array_copy, calls+1)
				}
				return safe
			}
		}
	} else {
		// Decrece
		for i := 0; i < len(report)-1; i++ {
			if report[i] <= report[i+1] || report[i]-report[i+1] > 3 {
				if calls < 2 {
					i++
					copy(array_copy, report)
					array_copy = append(array_copy[:i], array_copy[i+1:]...)
					safe = IsSafe(array_copy, calls+1)
				}
				return safe
			}
		}
	}
	return true
}

func SolutionOne(reports [][]int) int {
	safe := 0
	for _, report := range reports {
		if IsSafe(report, 1) {
			safe += 1
		} else {
			if IsSafe(report[1:], 2) {
				safe += 1
			}
		}
	}
	return safe
}

func main() {
	fileName := "input.txt"
	text := GetFileContent(fileName)

	var reports [][]int
	for _, each_ln := range text {
		reports = append(reports, ArrayAtoi(strings.Split(each_ln, " ")))
	}

	fmt.Println(SolutionOne(reports))
}
