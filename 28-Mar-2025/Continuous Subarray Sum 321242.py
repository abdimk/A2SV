# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums, k):
        prefix_mod = {0: -1} 
        total = 0  
        
        for i, num in enumerate(nums):
            total += num  
            mod = total % k if k != 0 else total  
            
            if mod in prefix_mod:
                if i - prefix_mod[mod] > 1:  
                    return True
            else:
                prefix_mod[mod] = i 
        
        return False
