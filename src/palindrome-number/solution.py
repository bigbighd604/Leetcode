#/bin/env python

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        a, b = x, 0
        while a > b:
            b = b * 10 + a % 10
            a = a / 10
        # x is a single digit number
        if a == 0:
            return x == b
        # even bits number (a == b), odd bits (a == b / 10)
        return a == b or a == b / 10

if __name__ == '__main__':
    input = [121,1221,1231,-1,1,999,0]
    expect = [True, True, False, False, True, True, True]
    s = Solution()
    for i, item in enumerate(input):
        result = s.isPalindrome(item)
        if result != expect[i]:
            print '%s Failed. Expect: %s, Got: %s' % (item, expect[i], not expect[i])
        else:
            print '%s Passed. Expect: %s, Got: %s' % (item, expect[i], result)

