# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))

        return max(nums) if len(nums) <3 else sorted(nums)[-3]
        