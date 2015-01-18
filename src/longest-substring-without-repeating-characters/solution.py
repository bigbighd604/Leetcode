#!/bin/env python

# Return size of longest substring and return the substring.

class Solution:
    def lengthWithDict(self, s):
        max = 0
        dict = {}
        last_repeat_pos = -1
        result_index = 0
        for i, char in enumerate(s):
            if char in dict and last_repeat_pos < dict[char]:
                last_repeat_pos = dict[char]
            if i - last_repeat_pos > max:
                max = i - last_repeat_pos
                # result index starts after last repeat position.
                result_index = last_repeat_pos + 1
            dict[char] = i
        return max,s[result_index:result_index+max]

    def lengthWithList2(self, s):
        max = 0
        result_index = 0
        temp_index = 0
        temp_length = 0
        for i, char in enumerate(s):
            if char in s[temp_index:i]:
                if temp_length > max:
                    result_index = temp_index
                    max = temp_length
                jump = s[temp_index:i].index(s[i]) + 1
                temp_index += jump
                temp_length = temp_length - jump + 1
            else:
                temp_length += 1
        if temp_length > max:
            result_index = temp_index
            max = temp_length
        return max, s[result_index:result_index+max]

    # @return an integer
    def lengthWithList(self, s):
        # Empty string
        if not s:
            return 0
        # Single character string
        if len(s) == 1:
            return 1
        # String length > 1
        result_index = 0
        longest_length = 1
        temp_index = 0
        temp_length = 1
        cursor = 1
        while cursor < len(s):
            if s[cursor] in s[temp_index:cursor]:
                #if len(s[temp_index:cursor]) > longest_length:
                if temp_length > longest_length:
                    result_index = temp_index
                    #longest_length = len(s[temp_index:cursor])
                    longest_length = temp_length
                jump = s[temp_index:cursor].index(s[cursor]) + 1
                temp_index += jump
                temp_length = temp_length - jump + 1
            else:
                temp_length += 1
            cursor += 1
        if temp_length > longest_length:
            result_index = temp_index
            longest_length = temp_length
        return longest_length, s[result_index:result_index+longest_length]


if __name__ == '__main__':
    s1 = "abcabcdbb"
    s2 = "bbbcdbb"
    s3 = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
    s4 = "abcdef"
    s5 = "bbbbbbbbb"
    s6 = "qopubjguxhxdipfzwswybgfylqvjzhar"
    s = Solution()
    print s.lengthWithList(s1)
    print s.lengthWithList(s2)
    print s.lengthWithList(s3)
    print s.lengthWithList(s4)
    print s.lengthWithList(s5)
    print s.lengthWithList(s6)

    print s.lengthWithList2(s1)
    print s.lengthWithList2(s2)
    print s.lengthWithList2(s3)
    print s.lengthWithList2(s4)
    print s.lengthWithList2(s5)
    print s.lengthWithList2(s6)

    print s.lengthWithDict(s1)
    print s.lengthWithDict(s2)
    print s.lengthWithDict(s3)
    print s.lengthWithDict(s4)
    print s.lengthWithDict(s5)
    print s.lengthWithDict(s6)

