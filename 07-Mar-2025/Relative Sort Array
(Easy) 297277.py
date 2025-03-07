# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []
        for i in arr2:
            res += ([i] * count[i])

        res.extend(sorted([x for x in arr1 if x not in arr2]))
        return res
        
