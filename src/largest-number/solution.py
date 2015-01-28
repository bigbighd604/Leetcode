#!/bin/env python

class Solution:
    # This method is not correct, will give out wrong result, i.e
    # A='22221122', B='222211' will return 0
    # but it can pass the 221 testcases.
    def compareLongShortStr(self, l, s):
        sl = len(s)
        ll = len(l)
        for i in range(ll):
            if l[i] > s[i % sl]:
                return 1
            elif l[i] < s[i % sl]:
                return -1
        mod = ll % sl
        if mod == 0:
            return 0
        i = 0
        j = mod
        while i < mod and j < sl:
            if l[i] > s[j]:
                return 1
            elif l[i] < s[j]:
                return -1
            i += 1
            j += 1
        return 0

    # Very elegent compare method for this problem
    # take advantage of builtin string comparasion
    def compareStr(self, A, B):
        if A+B > B+A:
            return 1
        elif A+B < B+A:
            return -1
        return 0

    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        # numStr = map(str, numStr)
        numStr = [str(i) for i in num]
        sortedStr = sorted(numStr, cmp=self.compareStr, reverse=True)
        if sortedStr[0] != '0':
            return ''.join(sortedStr)
        # catch the all '0' case
        return '0'

if __name__ == '__main__':
    s = Solution()
    s1 = '22221122'
    s2 = '222211'
    print s.compareLongShortStr('22221122', '222211')
    if s1+s2 > s2+s1:
        print '%s+%s' %(s1, s2)
    else:
        print '%s+%s' %(s2, s1)

