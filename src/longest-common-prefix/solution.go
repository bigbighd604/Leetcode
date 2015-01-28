package main

import (
  "fmt"
  "strings"
)

func longestCommonPrefix(stringSlice []string) string {
  length := len(stringSlice)
  if length == 0 { return "" }
  if length == 1 { return stringSlice[0] }
  // Because the result will be less than the shortest item.
  // Pick any element will work, first one is easy to traverse.
  str := stringSlice[0]
  for i := 0; i < len(str); i++ {
    for _, value := range stringSlice[1:] {
      // str[:i+1] contains [0, i]
      if strings.Index(value, str[:i+1]) != 0 {
        return str[:i]
      }
    }
  }
  return str
}

func main() {
  input := [][]string{
    {"aa", "a"},
    {"", ""},
    {"abcd", "abdef", "ab", "abdtf"},
  }
  output := []string{"a", "", "ab"}
  for i, strs := range input {
    r := longestCommonPrefix(strs)
    if r == output[i] {
      fmt.Println("Test Case Passed: ", i)
    } else {
      fmt.Println("Test Case Failed: ", i, " expect: ", output[i], " output: ", r)
    }
  }
}
