# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def isPalindrome(self, strs:str, left:int, right:int):
        while left < right:
            if strs[left] != strs[right]:
                return False
            left+=1
            right-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        left,right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)
            left+=1
            right-=1
        return True