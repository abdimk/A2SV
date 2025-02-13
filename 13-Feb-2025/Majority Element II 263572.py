# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        
        element_count = Counter(nums)
        
        majority_elements = []
        threshold = len(nums) // 3
        
        
        for element, count in element_count.items():
            
            if count > threshold:
                majority_elements.append(element)
        
        return majority_elements