class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        s1 = strs[0]
        # There is another way to go through all remain strs
        # and compare char by char, but need to take care of edge cases
        # like len(s) < len(s1), and also slower than the following method
        for i in range(len(s1)):
            for s in strs[1:]:
                if not s.startswith(s1[:i+1]):
                    return s1[:i]
        # This covers cases like ["", ""] and ["aa", "aa"]
        return s1
