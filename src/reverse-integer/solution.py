class Solution:
    def reverse2(self, x):
        # This way is faster than convert to str one by ~8ms.
        minus = False
        result = 0
        if x < 0:
            minus = True
            x = abs(x)
        while x != 0:
            n = x % 10
            if result > 0x7FFFFFFF / 10:
                return 0
            result = result * 10 + n
            x = x / 10
        if minus:
            return -result
        return result

    # @return an integer
    def reverse(self, x):
        minus = False
        if x < 0:
            minus = True
            x = abs(x)
        l = [ char for char in str(x)]
        size = len(l)
        mid = size / 2
        for i in xrange(mid): # Reverse
            l[i], l[size - 1 - i] = l[size - 1 - i], l[i]
        r = int(''.join(l)) # This will remove leading '0's.
        if r > 0x7FFFFFFF: # Check maximum signed int overflow
            return 0
        if minus:
            r = -r
        return r
