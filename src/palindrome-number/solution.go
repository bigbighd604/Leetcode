package main

import "fmt"

type Palindrome int

func (p Palindrome) isPalindrome() bool {
  x := int(p)
  if x == 0 { return true }
  if x < 0 || x % 10 == 0 { return false }
  a, b := x, 0
  for a > b {
    b = b * 10 + a % 10
    a /= 10
  }
  if a == 0 { return x == b }
  return a == b || a == b / 10
}


func main() {
  arr := []Palindrome {
    121, 1221, 1231, -1, 1,
  }
  for _, v := range arr {
    if v.isPalindrome() {
      fmt.Println(v, " is!")
    } else {
      fmt.Println(v, " is not!")
    }
  }
}
