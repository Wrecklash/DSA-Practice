"""
Problem: 485. Max Consecutive Ones
Difficulty: Easy
URL: https://leetcode.com/problems/max-consecutive-ones/

Description:
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Examples:
    Input: nums = [1,1,0,1,1,1]
    Output: 3

    Input: nums = [1,0,1,1,0,1]
    Output: 2

Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxcount = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count = count + 1
            else:
                if count > maxcount:
                    maxcount = count
                count = 0

        return max(maxcount, count)
