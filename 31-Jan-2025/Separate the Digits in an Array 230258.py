# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []

        for num in nums:
            for digit in str(num):
                answer.append(int(digit))

        return answer
