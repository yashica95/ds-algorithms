"""
Day 3. Roman to Integer
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = {
            'I' : 1,
            'V' : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        num = 0
        for i in range(0,len(s) - 1):
            if dict_roman[s[i]] < dict_roman[s[i+1]]:
                num -= dict_roman[s[i]]

            else:
                num += dict_roman[s[i]]

        return num + dict_roman[s[-1]]



        
