"""
Problem: 1365. How Many Numbers Are Smaller Than the Current Number
Difficulty: Easy
URL: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

Description:
Given the array nums, for each nums[i] find out how many numbers in the array are
smaller than it. Return the answer in an array.

Examples:
    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]

    Input: nums = [6,5,4,8]
    Output: [2,1,0,3]

    Input: nums = [7,7,7,7]
    Output: [0,0,0,0]

Constraints:
    2 <= nums.length <= 500
    0 <= nums[i] <= 100
"""


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        actual = nums[:]
        nums.sort()
        output = []
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if actual[i] == nums[j]:
                    output.append(j)
                    break
        return output
