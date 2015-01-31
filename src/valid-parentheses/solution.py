#!/bin/env python

class Solution:
    # @return a boolean
    def isValid(self, s):
        l = len(s)
        if l == 0 or l % 2 == 1:
            return False
        d = {'(': ')', '{': '}', '[': ']'}
        stack = [s[0]]
        for i in range(1, l):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                char = stack.pop()
                # Python will throw exception if char not in d
                # unlike C++ will insert and return default value.
                if char not in d or d[char] != s[i]:
                    return False
        if len(stack) > 0:
            return False
        return True

if __name__ == '__main__':
    input = '(){}[]'
    s = Solution()
    if s.isValid(input):
        print 'Passed'
