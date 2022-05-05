"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

A subarray is a contiguous part of an array.

"""
class Solution:
    def maxSubArray(self, nums:list) -> int:
        #kadane's algorithm
        #local_maximum at index i is the maximum of A[i] and the sum of A[i] and local_maximum at index i-1.

        for i in range(1,len(nums)):
            print(nums)
            nums[i] = max(nums[i], nums[i-1] + nums[i])

        print(max(nums))





Solution().maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4])
