# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                index = (i + nums[i]) % len(nums)
                result.append(nums[index])
            elif nums[i] == 0:
                result.append(nums[i])
            else:
                index = (i + nums[i]) % len(nums)
                result.append(nums[index])

        return result
