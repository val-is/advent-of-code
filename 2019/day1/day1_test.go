package main

import "testing"

func BenchmarkDay1Part2Iterative(b *testing.B) {
	inputs := getInputs("input.txt")
	for i := 0; i < b.N; i++ {
		part2Loop(inputs)
	}
}

func BenchmarkDay1Part2Recursive(b *testing.B) {
	inputs := getInputs("input.txt")
	for i := 0; i < b.N; i++ {
		part2Recursive(inputs)
	}
}
