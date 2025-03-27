# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        """
        let's just do the bruteforce method | can be solved using sliding window approch

        """

        res = 1
        n = len(s)

        for i in range(n - 1):
            for j in range(i+1, n):
                
                tmp = s[i:j+1]
                if self.helper(tmp):
                    res = max(res, j+1-i)
        return res

def helper(self, s):
        n = len(s)
        if n < 2:
            return True
            
        cnt = 0
        for i in range(1, n):
            if s[i] == s[i-1]:
                cnt+=1
        return cnt < 2



        