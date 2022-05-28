"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.


"""

class Solution:

    def majorityElement(self, nums: list) -> int:
        print(sorted(nums)[len(nums)//2])

    # O(n)space complexity using Hash map
    def majorityElement2(self, nums: list) -> int:
        count = {}
        res, maxCount= 0 ,0
        for n in nums:
            count[n] = 1 + count.get(n, 0 )
            res = n if count[n] >  maxCount else res
            maxCount = max(count[n], maxCount)

        print(res, maxCount)

    #Boyer Moore's algorithm 
    def majorityElement3(self, nums: list) -> int:








Solution().majorityElement2(nums = [3,2,3])
