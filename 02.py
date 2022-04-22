"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not."""

#Solution 1: Converting to string

class Solution:
    def isPalindrome(self, x: int) -> bool:
                x = str(x)

                if x == x[::-1]: #reverse the string
                    return True
                else:
                    return False

#Solution 2: Without converting to string

class Solution2:
    def isPalindrome(self, x: int) -> bool:
                x_int=x
                if x_int ==0:
                    return True
                elif x_int>=0 and (x_int%10 !=0):
                    new_num = x_int%10
                    while x//10>0:
                        x = x//10
                        new_num = new_num*10 + x%10
                        #print(x)
                        #print(new_num)

                    return new_num==x_int
                else:
                    return False
