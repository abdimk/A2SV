# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = -1

        for num in sorted(num_set, reverse=True):
            length = 0
            while num in num_set:
                length+=1
                num *= num

            if length > 1:
                max_length = max(max_length, length)

        return max_length