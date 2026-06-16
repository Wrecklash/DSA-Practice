"""
Problem: 636. Exclusive Time of Functions
Difficulty: Medium
URL: https://leetcode.com/problems/exclusive-time-of-functions/

Description:
Given n functions and a list of logs in format "{function_id}:{start|end}:{timestamp}",
return the exclusive execution time for each function.

Examples:
    Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
    Output: [3,4]

    Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
    Output: [8]

    Input: n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
    Output: [7,1]

Constraints:
    1 <= n <= 100
    2 <= logs.length <= 500
    0 <= function_id < n
    0 <= timestamp <= 10^9
"""


class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        results = [0] * n
        prev = 0
        stack = []
        for i in range(len(logs)):

            id, type, time = logs[i].split(":")
            id = int(id)
            time = int(time)

            if type == "start":
                if stack:
                    results[stack[-1]] += time - prev
                stack.append(id)
                prev = time
            else:
                results[stack[-1]] += time - prev + 1
                stack.pop()
                prev = time + 1
        return results


if __name__ == "__main__":
    s = Solution()

    tests = [
        ((2, ["0:start:0","1:start:2","1:end:5","0:end:6"]), [3,4]),
        ((1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]), [8]),
        ((2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]), [7,1]),
    ]

    for (n, logs), expected in tests:
        result = s.exclusiveTime(n, logs)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} | Expected: {expected} | Got: {result}")
