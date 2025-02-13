# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        ctr = Counter(nums)
        return nlargest(2, ctr, key = lambda x: ctr[x])