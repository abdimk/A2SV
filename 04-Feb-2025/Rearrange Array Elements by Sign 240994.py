# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i,j = 0,1

        result = [0] * len(nums)
        for k in range(len(nums)):
            if nums[k] > 0:
                result[i] = nums[k]
                i+=2
            else:
                result[j] = nums[k]
                j+=2
        
        return result
        