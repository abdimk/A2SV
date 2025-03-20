# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        New Trick  if you want to edit the array in place use arr[:]
        """

        p1 = 0
        p2 = len(arr)
        
        while p1 < p2:
            if arr[p1] == 0:
                arr.insert(p1+1, 0)
                p1+=1
            
            p1+=1

        if len(arr) != p2:
            arr[:] = arr[:p2]