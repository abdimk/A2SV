# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        num_str = str(abs(num))
        sorted_str = sorted(num_str) 

        if num > 0:
 
            if sorted_str[0] == "0":
                for i in range(len(sorted_str)):
                    if sorted_str[i] != "0":
                        sorted_str[0], sorted_str[i] = sorted_str[i], sorted_str[0]
                        break
            return int("".join(sorted_str))  
        
        else:
            return -int("".join(sorted(num_str, reverse=True)))  