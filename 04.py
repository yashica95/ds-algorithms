"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string """

class Solution:
    def longestCommonPrefix(self, m) -> str:
        if not m: return ''
        s1 = min(m)
        s2 = max(m)
        for i, c in enumerate(s1):
            #print(i,c)
            #print(s2[i])
            if c != s2[i]:
                return s1[:i]
        return s1


Solution().longestCommonPrefix(["flower","flow","flight"])
