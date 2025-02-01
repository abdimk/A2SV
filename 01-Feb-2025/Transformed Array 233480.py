# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res  = [0] * size

        for ind, val in enumerate(nums):
            res[ind] = nums[(ind + val) % size]

        return res