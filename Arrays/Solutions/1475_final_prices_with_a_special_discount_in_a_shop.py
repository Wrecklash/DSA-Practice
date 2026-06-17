"""
Problem: 1475. Final Prices With a Special Discount in a Shop
Difficulty: Easy
URL: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

Description:
Given an integer array prices where prices[i] is the price of the ith item
in a shop, there is a special discount for items in the shop. If you buy
the ith item, you will receive a discount equivalent to prices[j] where j
is the minimum index such that j > i and prices[j] <= prices[i]. If there
is no such index j, you will not receive any discount.
Return an integer array answer where answer[i] is the final price you will
pay for the ith item of the shop, considering the special discount.

Examples:
    Input: prices = [8,4,6,2,3]
    Output: [4,2,4,2,3]

    Input: prices = [1,2,3,4,5]
    Output: [1,2,3,4,5]

    Input: prices = [10,1,1,6]
    Output: [9,0,1,6]

Constraints:
    1 <= prices.length <= 500
    1 <= prices[i] <= 1000
"""


class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        flag = 0

        for i in range(len(prices)):
            current_price = prices[i]
            for j in range(i + 1, len(prices)):
                if current_price >= prices[j]:
                    stack.append(current_price - prices[j])
                    flag = 1
                    break

            if flag == 0:
                stack.append(current_price)
            flag = 0

        return stack


if __name__ == "__main__":
    s = Solution()

    tests = [
        ([8,4,6,2,3], [4,2,4,2,3]),
        ([1,2,3,4,5], [1,2,3,4,5]),
        ([10,1,1,6], [9,0,1,6]),
    ]

    for prices, expected in tests:
        result = s.finalPrices(prices)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} | prices={prices} | Expected: {expected} | Got: {result}")
