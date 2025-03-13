# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        plc = 0
        seeker= 0
        n = len(nums)

        while seeker < n:
            if nums[seeker] != 0:
                nums[plc],nums[seeker] = nums[seeker], nums[plc]
                plc+=1
            seeker+=1
        
        return nums