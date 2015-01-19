package main

import (
  "fmt"
  "flag"
)

type ListNode struct {
  val int
  next *ListNode
}

func addTwoNumbers(l1, l2 *ListNode) *ListNode {
  var result *ListNode = nil // Head
  carryOver := 0
  l1Cursor := l1
  l2Cursor := l2
  rCursor := &result // Pointer to pointer of ListNode
  for l1Cursor != nil && l2Cursor != nil {
    sum := l1Cursor.val + l2Cursor.val + carryOver
    carryOver = sum / 10
    tempSum := sum % 10
    l1Cursor, l2Cursor = l1Cursor.next, l2Cursor.next
    tNode := new(ListNode)
    tNode.val = tempSum
    *rCursor = tNode
    rCursor = &(tNode.next)
  }
  for l1Cursor != nil {
    sum := l1Cursor.val + carryOver
    carryOver = sum / 10
    tempSum := sum % 10
    l1Cursor = l1Cursor.next
    tNode := new(ListNode)
    tNode.val = tempSum
    *rCursor = tNode
    rCursor = &(tNode.next)
  }
  for l2Cursor != nil {
    sum := l2Cursor.val + carryOver
    carryOver = sum / 10
    tempSum := sum % 10
    l2Cursor = l2Cursor.next
    tNode := new(ListNode)
    tNode.val = tempSum
    *rCursor = tNode
    rCursor = &(tNode.next)
  }
  if carryOver > 0 {
    tNode := new(ListNode)
    tNode.val = carryOver
    *rCursor = tNode
  }

  return result
}


func main() {
  wordPtr := flag.String("word", "foo", "a string")
  numbPtr := flag.Int("numb", 42, "an int")
  boolPtr := flag.Bool("fork", false, "a bool")
  var svar string
  flag.StringVar(&svar, "svar", "bar", "a string var")
  flag.Parse()

  fmt.Println("word:", *wordPtr)
  fmt.Println("numb:", *numbPtr)
  fmt.Println("fork:", *boolPtr)
  fmt.Println("svar:", svar)
  fmt.Println("tail:", flag.Args())

  l1 := ListNode{
    2,
    &ListNode{
      4,
      &ListNode{
        3,
        nil,
      },
    },
  }
  l2 := ListNode{
    5,
    &ListNode{
      6,
      &ListNode{
        4,
        nil,
      },
    },
  }
  r := addTwoNumbers(&l1, &l2)
  for r != nil {
    fmt.Println(r.val)
    r = r.next
  }
}
