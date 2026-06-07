"""
Problem: 1470. Shuffle the Array
Difficulty: Easy
URL: https://leetcode.com/problems/shuffle-the-array/

Description:
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Examples:
    Input: nums = [2,5,1,3,4,7], n = 3
    Output: [2,3,5,4,1,7]

    Input: nums = [1,2,3,4,4,3,2,1], n = 4
    Output: [1,4,2,3,3,2,4,1]

    Input: nums = [1,1,2,2], n = 2
    Output: [1,2,1,2]
"""

class Solution(object):

    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans

            
        
