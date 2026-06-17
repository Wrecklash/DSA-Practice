"""
Problem: 739. Daily Temperatures
Difficulty: Medium
URL: https://leetcode.com/problems/daily-temperatures/

Description:
Given an array of integers temperatures representing daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature. If there is no
future day for which this is possible, keep answer[i] == 0.

Examples:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]

    Input: temperatures = [30,60,90]
    Output: [1,1,0]

Constraints:
    1 <= temperatures.length <= 10^5
    30 <= temperatures[i] <= 100
"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        results = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                waiting_index = stack.pop()
                results[waiting_index] = i - waiting_index
            stack.append(i)

        return results


if __name__ == "__main__":
    s = Solution()

    tests = [
        ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
        ([30,40,50,60], [1,1,1,0]),
        ([30,60,90], [1,1,0]),
    ]

    for temperatures, expected in tests:
        result = s.dailyTemperatures(temperatures)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} | temperatures={temperatures} | Expected: {expected} | Got: {result}")
