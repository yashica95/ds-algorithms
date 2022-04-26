"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        pair_brackets = {
        "(": ")",
        "[" :"]",
        "{" : "}"
        }

        stack =[]
        for char in s:
            print(stack)
            if char in pair_brackets.keys():
                stack.append(char)
            elif char in pair_brackets.values():
                if stack==[] or char != pair_brackets[stack.pop()]:
                    return False
            else:
                return False
        return stack==[]

Solution().isValid("()()[]")
