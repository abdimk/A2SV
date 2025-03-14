# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        size = len(nums)
        counter = 0

        for i in range(size):
            for j in range(size):
                if i < j and  nums[i] + nums[j] < target:
                    counter+=1

        return counter
        

        