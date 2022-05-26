"""

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

"""


class Solution:
    def getRow(self, rowIndex: int) -> list:

        row = [1]
        for i in range(rowIndex):
            row = [x + y for x,y in zip([0]+row, row + [0])]

        return row






Solution().getRow(rowIndex=5)
