"""

Given an integer numRows, return the first numRows of Pascal's triangle.

"""
class Solution:
    def generate(self, numRows: int) -> list:

        final_list = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                final_list[i][j] = final_list[i-1][j-1] + final_list[i-1][j]

        print(final_list)








Solution().generate(numRows=5)
