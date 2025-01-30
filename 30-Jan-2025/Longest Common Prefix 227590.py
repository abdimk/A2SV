# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        sort = sorted(strs)
        first = sort[0]
        last = sort[len(sort)-1]

        min_len = len(first)
        min_len = len(first) if len(first) < len(last) else len(last)

        for i in range(min_len):
            if(first[i] != last[i]):
                return result
            result+=first[i]

        return result
