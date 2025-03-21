# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1 = 0
        res = 10**308  # fancy way to express float('inf')
        s = 0
        n = len(nums)

        for p2 in range(n):
            s+=nums[p2]

            while s >= target:
                res = min(res, p2-p1+1)
                s-=nums[p1]
                p1+=1

        return 0 if res == 10**308 else res