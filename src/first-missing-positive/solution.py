#!/bin/env python

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        s = set()
        max = 0
        # Put positive number in a set, and record the max one.
        for v in A:
            if v > 0:
                s.add(v)
                if v > max:
                    max = v
        # No positive number left, 1 is the missing one.
        if not s:
            return 1
        # Test 1 to max, if not in set, then it's the missing one.
        for i in range(1, max+1)
            if i not in s:
                return i
        # cover cases when set includes contigous number start from 1.
        return max+1

    # Extra n space
    def firstMissingPositive2(self, A):
        length = len(A)
        if length == 0:
            return 1
        markList = [False for i in xrange(length)]
        for i, v in enumerate(A):
            if v > 0 and v <= length and not markList[v-1]:
                markList[v-1] = True
        for i, v in enumerate(markList):
            if not v:
                return i+1
        return length+1

    # In place modify list A
    def firstMissingPositive2(self, A):
        length = len(A)
        if length == 0:
            return 1
        for i in range(length):
            v = A[i]
            # Recursive place value v to position [v-1]
            while v > 0 and v <= length and A[v-1] != v:
                A[i], A[v-1] = A[v-1], A[i]
                v = A[i]
        for i, v in enumerate(A):
            if v != i+1:
                return i+1 
        return length+1
