# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
        
        current_max = 0
        result = 0
        for key, value in count.items():
            if value > current_max:
                current_max = value
                result = key
                
        return result