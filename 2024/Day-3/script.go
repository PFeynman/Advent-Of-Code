package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func ArrayAtoi(array []string) (result []uint64) {
	for _, e := range array {
		x, _ := strconv.ParseUint(e, 10, 64)
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

func SolutionOne(memory string) uint64 {
	mul_re := regexp.MustCompile(`mul\(\d{1,3},\d{1,3}\)`)
	factors_re := regexp.MustCompile(`\d{1,3}`)
	multiplications := mul_re.FindAllString(memory, -1)

	var sum uint64 = 0
	var factors []uint64
	for _, mul := range multiplications {
		factors = ArrayAtoi(factors_re.FindAllString(mul, -1))
		sum += factors[0] * factors[1]
	}

	return sum
}

func SolutionTwo(memory string) uint64 {
	do_pos := strings.Index(memory, "do()")
	dont_pos := strings.Index(memory, "don't()")

	for dont_pos > -1 {
		for do_pos < dont_pos {
			memory = strings.Replace(memory, memory[do_pos:do_pos+4], "", 1)
			do_pos = strings.Index(memory, "do()")
			dont_pos -= 4
		}
		memory = strings.Replace(memory, memory[dont_pos:do_pos+4], "", 1)
		dont_pos = strings.Index(memory, "don't()")
		do_pos = strings.Index(memory, "do()")
	}

	return SolutionOne(memory)
}

func main() {
	fileName := "input.txt"
	text := GetFileContent(fileName)
	memory := strings.Join(text, "")

	fmt.Printf("Solution One: %d\n", SolutionOne(memory))
	fmt.Printf("Solution Two: %d\n", SolutionTwo(memory))
}
