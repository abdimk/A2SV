# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        unique = set()
        i = 0
        for j in range(len(nums)):
            while nums[j] in unique:
                curr -= nums[i]
                unique.remove(nums[i])
                i+=1
            unique.add(nums[j])
            curr += nums[j]
            res = max(res, curr)

        return res
