package main

import "fmt"


func firstMissingPositive(A []int) int {
  length := len(A)
  if length == 0 {
    return 1
  }
  // slice will be initialized to 0.
  markList := make([]int, length)
  for _, v := range A {
    if v > 0 && v <= length && markList[v-1] != 1 {
      markList[v-1] = 1
    }
  }
  for i, v := range markList {
    if v != 1 {
      return i+1
    }
  }
  return length+1
}

func main() {
  l1 := []int {1, 2, 0}
  l2 := []int {3, 4, -1, 1}
  l3 := []int {1}
  l4 := []int {}

  fmt.Println(firstMissingPositive(l1))
  fmt.Println(firstMissingPositive(l2))
  fmt.Println(firstMissingPositive(l3))
  fmt.Println(firstMissingPositive(l4))
}
