package main

import (
  "fmt"
)

type S string

func (s S) isValid() bool {
  l := len(s)
  if l == 0 || l % 2 == 1 { return false }
  // Here can use byte or uint8, but can not use rune
  // because rune == int32, byte == uint8, and s[i] returns
  // a uint8 type value.
  m := map[byte]byte{
    '(': ')', '{': '}', '[': ']',
  }
  stack := []byte{s[0]}
  for i := 1; i < l; i++ {
    if s[i] == '(' || s[i] == '{' || s[i] == '[' {
      stack = append(stack, s[i])
    } else {
      var char byte
      // Go slice doesn't have pop function like Python, need to
      // use the following way to simulate a pop from slice end.
      char, stack = stack[len(stack) - 1], stack[:len(stack) -1]
      if _, ok := m[char]; ok == false || m[char] != s[i] {
        return false
      }
    }
  }
  if len(stack) > 0 { return false }
  return true
}

func main() {
  var s1 S = "(){}[](([{}]))"
  if s1.isValid() {
    fmt.Println("Passed")
  } else {
    fmt.Println("Failed")
  }
}
