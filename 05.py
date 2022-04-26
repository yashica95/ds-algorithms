"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        list_accepted = ["()", "[]", "{}"]
        #start from the middle
        i = len(s)//2
        while i>0:
            i =len(s)//2
            if i%2 ==0 :

                print(i)
                if s not in list_accepted:
                    if (s[i] + s[i+1] in list_accepted):
                        s = s[0 : i : ] + s[i + 2 : :]
                        print(s)
                        #i -=1
                    else:
                        i=0
                        return False
                else:
                    i=0
                    return True

            else:
                #print(i)
                if s not in list_accepted:
                    if (s[i-1] + s[i] in list_accepted):
                        s = s[0 : i-1: ] + s[i + 1 : :]
                        print(s)
                    else:
                        i=0
                        return False
                        #i -=1
                else:
                    i=0
                    return True

Solution().isValid("()()[]")
