# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:

        n = len(arr)
        result = []


        def flip(idx):
            for i in range(0, idx//2 + 1):
                temp = arr[i]
                arr[i] = arr[idx - i]
                arr[idx - i] = temp
        

        for i in range(n - 1, 0, -1):
            for j in range(1,i+1):
                if arr[j] == i + 1:
                    flip(j)
                    result.append(j+1)

            flip(i)
            result.append(i+1)
        return result
            
        