# Problem: Merge Sorted Array - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_arr = nums1[:m]
        right_arr = nums2[:n]
        
        i, j = 0,0
        k = 0  # m + n
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                nums1[k] = left_arr[i]
                i+=1
                k+=1
            else:
                nums1[k] = right_arr[j]
                j+=1
                k+=1

        while i < len(left_arr):
            nums1[k] = left_arr[i]
            i+=1
            k+=1

        while j < len(right_arr):
            nums1[k] = right_arr[j]
            j+=1
            k+=1