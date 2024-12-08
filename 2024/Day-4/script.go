package main

import (
	"bufio"
	"fmt"
	"os"
	"reflect"
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

func SolutionOne(text []string) int {
	sum := 0
	for i, line := range text {
		for j, c := range line {
			if string(c) == "X" {
				// Horizontal
				if j <= len(line)-4 {
					if string(line[j+1]) == "M" && string(line[j+2]) == "A" && string(line[j+3]) == "S" {
						sum++
					}
				}
				// Horizontal hacia atrás
				if j >= 3 {
					if string(line[j-1]) == "M" && string(line[j-2]) == "A" && string(line[j-3]) == "S" {
						sum++
					}
				}
				// Vertical hacia abajo
				if i <= len(text)-4 {
					if string(text[i+1][j]) == "M" && string(text[i+2][j]) == "A" && string(text[i+3][j]) == "S" {
						sum++
					}
				}
				// Vertical hacia arriba
				if i >= 3 {
					if string(text[i-1][j]) == "M" && string(text[i-2][j]) == "A" && string(text[i-3][j]) == "S" {
						sum++
					}
				}
				// Diagonal abajo derecha
				if j <= len(line)-4 && i <= len(text)-4 {
					if string(text[i+1][j+1]) == "M" && string(text[i+2][j+2]) == "A" && string(text[i+3][j+3]) == "S" {
						sum++
					}
				}
				// Diagonal abajo izquierda
				if j >= 3 && i <= len(text)-4 {
					if string(text[i+1][j-1]) == "M" && string(text[i+2][j-2]) == "A" && string(text[i+3][j-3]) == "S" {
						sum++
					}
				}
				// Diagonal arriba derecha
				if j <= len(line)-4 && i >= 3 {
					if string(text[i-1][j+1]) == "M" && string(text[i-2][j+2]) == "A" && string(text[i-3][j+3]) == "S" {
						sum++
					}
				}
				// Diagonal arriba izquierda
				if j >= 3 && i >= 3 {
					if string(text[i-1][j-1]) == "M" && string(text[i-2][j-2]) == "A" && string(text[i-3][j-3]) == "S" {
						sum++
					}
				}
			}
		}
	}

	return sum
}

func SolutionTwo(text []string) int {
	templates := []string{"M.M.A.S.S", "S.S.A.M.M", "M.S.A.M.S", "S.M.A.S.M"}
	mask := []bool{true, false, true, false, true, false, true, false, true}

	test := ""
	var result []bool

	sum := 0
	for row := 1; row < len(text)-1; row++ {
		for col := 1; col < len(text[0])-1; col++ {
			test += string(text[row-1][col-1])
			test += string(text[row-1][col])
			test += string(text[row-1][col+1])
			test += string(text[row][col-1])
			test += string(text[row][col])
			test += string(text[row][col+1])
			test += string(text[row+1][col-1])
			test += string(text[row+1][col])
			test += string(text[row+1][col+1])

			for _, template := range templates {
				result = nil
				for i := 0; i < len(test); i++ {
					result = append(result, template[i] == test[i])
				}
				if reflect.DeepEqual(result, mask) {
					sum++
					break
				}
			}
			test = ""
		}
	}

	return sum
}

func main() {
	fileName := "input.txt"
	text := GetFileContent(fileName)

	fmt.Println(SolutionTwo(text))
}
