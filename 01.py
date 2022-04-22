"""

Day 1. Count Odd Numbers in an Interval Range

"""

#Solution 1 - O(n) complexity
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        j = 0
        for i in range(low, high+1):
            if i%2!=0:
                j +=1
        return j

#Solution 2 - O(1) complexity
class Solution2:
    def countOdds(self, low: int, high: int) -> int:
        if low%2 ==1 or high%2==1:
            return (high- low)//2 + 1
        else:
            return (high- low)//2
