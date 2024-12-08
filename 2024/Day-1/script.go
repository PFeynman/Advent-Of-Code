package main

import (
	"bufio"
	"cmp"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func Insert[T cmp.Ordered](ts []T, t T) []T {
	i, _ := slices.BinarySearch(ts, t)
	ts = append(ts, *new(T))
	copy(ts[i+1:], ts[i:])
	ts[i] = t
	return ts
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func Count(slice []int, needle int) int {
	count := 0
	for i := 0; i < len(slice); i++ {
		if slice[i] == needle {
			count += 1
		}
	}
	return count
}

func main() {
	fileName := "input.txt"
	file, err := os.Open(fileName)
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)

	scanner.Split(bufio.ScanLines)
	var text []string

	for scanner.Scan() {
		text = append(text, scanner.Text())
	}

	file.Close()

	var first_list []int
	var second_list []int
	for _, each_ln := range text {
		for j, value := range strings.Split(each_ln, "   ") {
			num, _ := strconv.Atoi(value)
			if j%2 == 0 {
				first_list = Insert(first_list, num)
			} else {
				second_list = Insert(second_list, num)
			}
		}
	}

	sum := 0
	for i := 0; i < len(text); i++ {
		sum += Abs(first_list[i] - second_list[i])
	}

	fmt.Println(sum)

	m := make(map[int]int)
	sum = 0
	for i := 0; i < len(text); i++ {
		_, ok := m[first_list[i]]
		if !ok {
			m[first_list[i]] = Count(second_list, first_list[i])
		}
		sum += first_list[i] * m[first_list[i]]
	}

	fmt.Println(sum)
}
