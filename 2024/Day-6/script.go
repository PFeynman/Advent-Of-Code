package main

import (
	"bufio"
	"fmt"
	"os"
)

type Position struct {
	i int
	j int
}

type Direction int

const (
	up Direction = iota
	right
	down
	left
)

var moveDir = map[Direction]string{
	up:    "^",
	right: ">",
	down:  "v",
	left:  "<",
}

func (dd Direction) String() string {
	return moveDir[dd]
}

func transition(d Direction) Direction {
	switch d {
	case up:
		return right
	case right:
		return down
	case down:
		return left
	case left:
		return up
	default:
		panic(fmt.Errorf("unknown move: %s", d))
	}
}

func GetFileContent(fileName string) (byteText [][]byte) {
	var text []string
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

	byteText = make([][]byte, len(text))
	for i, str := range text {
		byteText[i] = []byte(str)
	}

	return byteText
}

func FindStart(text [][]byte) Position {
	for i := 0; i < len(text); i++ {
		for j := 0; j < len(text[0]); j++ {
			if string(text[i][j]) == up.String() {
				return Position{i, j}
			}
		}
	}
	return Position{0, 0}
}

func printMap(text [][]byte) {
	for i := 0; i < len(text); i++ {
		for j := 0; j < len(text[0]); j++ {
			fmt.Print(string(text[i][j]))
		}
		fmt.Println()
	}
}

func Patrol(text [][]byte, currentPosition Position) {
	direction := up
	var nextPosition Position
	sum := 0
	for {
		switch direction {
		case up:
			nextPosition = Position{currentPosition.i - 1, currentPosition.j}
		case down:
			nextPosition = Position{currentPosition.i + 1, currentPosition.j}
		case right:
			nextPosition = Position{currentPosition.i, currentPosition.j + 1}
		case left:
			nextPosition = Position{currentPosition.i, currentPosition.j - 1}
		}

		if nextPosition.i < 0 || nextPosition.i > len(text)-1 || nextPosition.j < 0 || nextPosition.j > len(text[0])-1 {
			text[currentPosition.i][currentPosition.j] = 'X'
			sum++
			break
		} else if text[nextPosition.i][nextPosition.j] == '#' {
			direction = transition(direction)
		} else {
			if text[currentPosition.i][currentPosition.j] != 'X' {
				sum++
			}
			text[currentPosition.i][currentPosition.j] = 'X'
			currentPosition = nextPosition
		}
	}
	fmt.Println(sum)
}

func main() {
	fileName := "input.txt"
	text := GetFileContent(fileName)

	initialPosition := FindStart(text)

	Patrol(text, initialPosition)

}
