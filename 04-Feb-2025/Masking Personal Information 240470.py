# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            n, d = s.split("@")
            n, d = n.lower() , d.lower()
            n = n[0]+"*****"+n[-1]
            return n+"@"+d
        else:
            pn= ""
            for x in s:
                if x.isdigit():
                    pn+=x

            l = len(pn)
            if l > 10:
                return "+"+"*"*(l-10)+"-***-***-"+pn[-4:]
            return "***-***-"+pn[-4:]
        