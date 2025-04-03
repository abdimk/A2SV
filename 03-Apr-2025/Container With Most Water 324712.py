# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1

        while left < right:
            #  find area 
            # area = length * width // width * height

            current_area = (right - left) * min(height[left], height[right])
            result = max(result, current_area)
            (left := left + 1 ) if height[left] < height[right] else (right := right - 1)

        return result 
        