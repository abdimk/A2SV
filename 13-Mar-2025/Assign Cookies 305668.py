# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #size of cookie >= greed factor j => i
        #maximize the number of content and oput num 

        g.sort()
        s.sort()

        i = j = 0
        while i < len(g):
            while j < len(s) and g[i] > s[j]:
                j+=1
            if j == len(s):
                break


            i+=1
            j+=1

        return i