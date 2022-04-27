"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

"""


class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        startIndex =0
        count = 0
        for x in nums:
            if x!= val:
                nums[startIndex] = x
                startIndex +=1
            else:
                count +=1



        return startIndex




Solution().removeElement(nums = [3,2,2,3], val = 3)
