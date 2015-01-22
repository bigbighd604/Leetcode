package main

import "fmt"

const IntMax = 2147483647
const IntMin = -IntMax - 1

func reverse(x int) int {
  result := 0
  var n int
  for x != 0 {
    n = x % 10
    if result > IntMax / 10 || result < IntMin / 10 {
      return 0
    }
    result = result * 10 + n
    x = x / 10
  }
  return result
}

func main() {
  fmt.Println(reverse(123))
  fmt.Println(reverse(-123))
  fmt.Println(reverse(-100))
  fmt.Println(reverse(1463847412))
  fmt.Println(reverse(1463847412))
  fmt.Println(reverse(1000000003))
}

