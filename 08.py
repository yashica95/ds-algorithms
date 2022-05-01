
"""
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        else:
            return haystack.find(needle)



class Solution2:
    def strStr(self, haystack:str, needle:str)->int:
        if needle=="":
            return 0
        else:
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i] != needle[0]:
                    continue
                else:
                    if haystack[i:i+len(needle)] == needle:
                        return i
            return -1


Solution2().strStr(haystack='hello', needle="d")
