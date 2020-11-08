package main

import (
	"bufio"
	"io"
	"log"
	"os"
	"strconv"
)

func main() {
	inputs := getInputs("input.txt")

	log.Printf("Part 1: %d", part1(inputs))
	log.Printf("Part 2 iterative: %d", part2Loop(inputs))
}

func getInputs(filename string) []int64 {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatalf("%s", err)
	}
	defer file.Close()
	var inputs []int64
	reader := bufio.NewReader(file)
	for {
		line, err := reader.ReadBytes('\n')
		if err != nil && err != io.EOF {
			log.Fatalf("%s", err)
		}
		if len(line) > 0 {
			i, err := strconv.Atoi(string(line[:len(line)-1]))
			if err != nil {
				log.Fatalf("%s", err)
			}
			inputs = append(inputs, int64(i))
		}
		if err == io.EOF {
			break
		}
	}
	return inputs
}

func massToFuel(mass int64) int64 {
	if m := (mass / 3) - 2; m >= 0 {
		return m
	}
	return 0
}

func part1(inputs []int64) int64 {
	var sum int64
	for _, v := range inputs {
		sum += massToFuel(v)
	}
	return sum
}

func part2Loop(inputs []int64) int64 {
	var sum int64
	for _, v := range inputs {
		sum += func(mass int64) int64 {
			var sum int64
			for sum = -mass; mass > 0; mass = massToFuel(mass) {
				sum += mass
			}
			return sum
		}(v)
	}
	return sum
}

func part2Recursive(inputs []int64) int64 {
	var s int64
	for _, v := range inputs {
		s += calcDeadMassRecur(v)
	}
	return s
}

func calcDeadMassRecur(mass int64) int64 {
	fuel := massToFuel(mass)
	if fuel == 0 {
		return 0
	}
	return fuel + calcDeadMassRecur(fuel)
}
