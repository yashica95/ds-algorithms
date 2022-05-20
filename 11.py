
"""
Given a string s consisting of some words separated by some number of spaces,
return the length of the last word in the string.

"""



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        s = s.rstrip()
        print(s)
        if len(s) ==1:
            count= 1
        else:
            try:
                while s[-1] != " ":
                    count +=1
                    s = s[:-1]
            except:
                print(count)


        print(count)

Solution().lengthOfLastWord("day")
