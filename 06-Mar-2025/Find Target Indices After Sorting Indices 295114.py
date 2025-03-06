# Problem: Find Target Indices After Sorting Indices - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)

        for i in range(size - 1):
            min_index = i

            for j in range(i + 1, size):
                if nums[j] < nums[min_index]:
                    min_index = j

            nums[i],nums[min_index] = nums[min_index],nums[i]

        
        if target in nums:
            return [x[0] for x in enumerate(nums) if x[1] == target]
        else:
            return []
        