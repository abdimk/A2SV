# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        val_idx = {val : idx for idx, val in enumerate(nums)}
        for a, b in operations:
            nums[val_idx[a]] = b
            val_idx[b] = val_idx.pop(a)
        return nums  