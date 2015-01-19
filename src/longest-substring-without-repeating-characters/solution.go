package main

import (
  "fmt"
  "os"
)

func longestSubString2(s string) int {
  max := 0
  var table [256]int
  for i := 0; i < 256; i++ {
    table[i] = -1
  }
  last_repeat_pos := -1

  for i, char := range s {
    if table[char] != -1 && last_repeat_pos < table[char] {
      last_repeat_pos = table[char]
    }
    if i - last_repeat_pos > max {
      max = i - last_repeat_pos
    }
    table[char] = i
  }
  return max
}

func longestSubString(s string) int {
  max := 0
  m := make(map[rune]int)
  last_repeat_pos := -1

  for i, char := range s {
    if pos, ok := m[char]; ok && last_repeat_pos < pos {
      last_repeat_pos = pos
    }
    if i - last_repeat_pos > max {
      max = i - last_repeat_pos
    }
    m[char] = i
  }
  return max
}

func main() {
  s := "abcabcbb"
  fmt.Println(longestSubString(s))
  fmt.Println(longestSubString2(s))
  s = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
  fmt.Println(longestSubString(s))
  fmt.Println(longestSubString2(s))
  s = "qopubjguxhxdipfzwswybgfylqvjzhar"
  fmt.Println(longestSubString(s))
  fmt.Println(longestSubString2(s))
  argsWithoutProg := os.Args[1:]
  if len(argsWithoutProg) >= 1 {
    fmt.Println(longestSubString(argsWithoutProg[0]))
    fmt.Println(longestSubString2(argsWithoutProg[0]))
  }
}
