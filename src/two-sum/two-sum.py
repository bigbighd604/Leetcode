#!/bin/env python

class Solution:
    # @return a tuple, (index1, index2)
    # o(n^2) runtime complexity, o(1) space
    def twoSum(self, num, target):
        for i, value in enumerate(num):
            for j in range(i+1, len(num)):
                if value+num[j] == target:
                    return (i+1, j+1)

    # o(n) runtime complexity, o(n) space
    # dict store value -> index mapping
    def twoSumFast(self, num, target):
        result = {}
        for i, value in enumerate(num):
            if value not in result:
                result[target - value] = i
            else:
                return (result[value]+1, i+1)

if __name__ == '__main__':
    num = [2, 7, 11, 15]
    num2 = [ 2 * i for i in xrange(10240)]
    s = Solution()
    print s.twoSum(num, 9)
    print s.twoSum(num, 13)
    print s.twoSum(num, 18)
    print s.twoSum(num, 26)
    print s.twoSumFast(num2, 40000)
    print s.twoSum(num2, 40000)

