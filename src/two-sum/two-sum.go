package main

import "fmt"

func twoSum(nums []int, target int) (int, int) {
  // var m map[int]int
  m := make(map[int]int)
  var result [2]int
  for key, value := range nums {
    if index1, ok := m[value]; ok {
      // return index1 + 1, key + 1
      result[0] = index1 + 1
      result[1] = key + 1
    }
    m[target - value] = key
  }
  // have to return at the end of func
  return result[0], result[1]
}

func main() {
  nums := []int {1, 2, 4, 7, 11, 15}
  fmt.Println(twoSum(nums, 9))
}
