"""
Problem: 1929. Concatenation of Array
Difficulty: Easy
URL: https://leetcode.com/problems/concatenation-of-array/

Description:
Given an integer array nums of length n, you want to create an array ans of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

Examples:
    Input: nums = [1,2,1]
    Output: [1,2,1,1,2,1]

    Input: nums = [1,3,2,1]
    Output: [1,3,2,1,1,3,2,1]
"""

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Your solution here
        pass
