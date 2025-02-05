# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:


        maxp = sorted(nums)

        return max(maxp[-1]*maxp[-2]*maxp[-3], maxp[0]*maxp[1]*maxp[-1])