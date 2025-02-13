# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        pair_count = 0
        remove_count = 0

        for i in range(len(nums)):
            dic[nums[i]] += 1
            if(dic[nums[i]] == 2):
                dic[nums[i]] -= 2
                pair_count += 1
                remove_count += 2
        
        return [pair_count, len(nums) - remove_count]