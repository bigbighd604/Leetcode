#!/bin/env python

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getValueAndMove(self, l): 
        r = 0 
        if l:
            r = l.val
            l = l.next
        return r, l

    # Although code is much clear and simple,
    # this method is slower than addTwoNumbers by ~30ms in leetcode,
    # probably due to the extra function calls.
    def addTwoNumbers2(self, l1, l2):
        carry_over = 0 
        result = ListNode(-1) # head, will not use
        result_cursor = result
        while l1 or l2: 
            l1_val, l1 = self.getValueAndMove(l1)
            l2_val, l2 = self.getValueAndMove(l2)
            carry_over, temp_sum = divmod(l1_val + l2_val + carry_over, 10) 
            # can not use the following statement
            # result_cursor = result_cursor.next = ListNode(temp_sum)
            # the above statement will break the link between result and result_cursor.
            result_cursor.next = ListNode(temp_sum)
            result_cursor = result_cursor.next
        if carry_over > 0:
            result_cursor.next = ListNode(carry_over)
        return result.next

    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry_over = 0
        result = ListNode(-1) # head, will not use
        l1_cursor = l1
        l2_cursor = l2
        result_cursor = result
        while l1_cursor and l2_cursor:
            carry_over, temp_sum = divmod(l1_cursor.val + l2_cursor.val + carry_over, 10)
            l1_cursor, l2_cursor = l1_cursor.next, l2_cursor.next
            # can not use the following statement
            # result_cursor = result_cursor.next = ListNode(temp_sum)
            # the above statement will break the link between result and result_cursor.
            result_cursor.next = ListNode(temp_sum)
            result_cursor = result_cursor.next
        while l2_cursor:
            carry_over, temp_sum = divmod(l2_cursor.val + carry_over, 10)
            l2_cursor = l2_cursor.next
            result_cursor.next = ListNode(temp_sum)
            result_cursor = result_cursor.next
        while l1_cursor:
            carry_over, temp_sum = divmod(l1_cursor.val + carry_over, 10)
            l1_cursor = l1_cursor.next
            result_cursor.next = ListNode(temp_sum) 
            result_cursor = result_cursor.next
        if carry_over > 0:
            result_cursor.next = ListNode(carry_over)
        return result.next

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(0)
    l2 = ListNode(0)
    r = s.addTwoNumbers(l1, l2)
    result = []
    while r:
        result.append(r.val)
        r = r.next
    print result
