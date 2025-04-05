# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr:
            return 0

        n = len(arr)
        res = 1
        l = 0

        for r in range(1, n):
            cmp = (arr[r - 1] > arr[r]) - (arr[r - 1] < arr[r])
            
            if cmp == 0:
                l = r
            elif r == n - 1 or (cmp * ((arr[r] > arr[r + 1]) - (arr[r] < arr[r + 1]))) != -1:
                res = max(res, r - l + 1)
                l = r
        
        return res